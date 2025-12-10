#!/usr/bin/env python

import argparse
import datetime
import os
import os.path
import json
import inspect
import importlib
import pkgutil

import dsl
import tests
import solvers

def get_data(train=True):
    path = f'ARC-AGI/data/{"training" if train else "evaluation"}'
    data = {}
    for fn in os.listdir(path):
        if os.path.splitext(fn)[1] == '.json':
            with open(f'{path}/{fn}') as f:
                data[fn.rstrip('.json')] = json.load(f)
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'train': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }


def get_functions(path):
    """ returns a list of available functions """
    paths = []
    root = os.path.dirname(path) if os.path.basename(path) == '__init__.py' else path
    if os.path.isdir(root):
        for entry in os.listdir(root):
            if not entry.endswith('.py'):
                continue
            paths.append(os.path.join(root, entry))
    else:
        paths.append(root)

    functions = []
    for file_path in paths:
        with open(file_path, 'r') as f:
            code = f.read()
        for row in code.split('\n'):
            if row.startswith('def '):
                function = row.split('def ')[1].split('(')[0]
                functions.append(function)
    return functions


def run_dsl_tests(dsl_module, test_module):
    """ test DSL primitives """
    dsl_functions = get_functions(dsl_module.__file__)
    test_functions = get_functions(test_module.__file__)
    expected = set([f'test_{f}' for f in dsl_functions])
    assert set(test_functions) == expected
    for fun in test_functions:
        getattr(test_module, fun)()


def test_solvers_formatting(solvers_module, dsl_module):
    """ tests the implementd solvers for formatting """
    with open('constants.py', 'r') as f:
        constants = [c.split(' = ')[0] for c in f.readlines() if ' = ' in c]
    definitions = {}
    for module_info in pkgutil.iter_modules(solvers_module.__path__):
        if module_info.name.startswith("_"):
            continue
        module = importlib.import_module(f"{solvers_module.__name__}.{module_info.name}")
        definitions[module_info.name] = inspect.getsource(module.solve)
    dsl_interface = get_functions(dsl_module.__file__)
    n_correct = 0
    n = len(definitions)
    for key, definition in definitions.items():
        try:
            lines = definition.split('\n')
            assert lines[0] == 'def solve(I):'
            assert lines[-1] == ''
            variables = set()
            calls = set()
            for line in lines[1:-2]:
                variable, call = line.lstrip().split(' = ')
                function, args = call.split('(')
                assert variable not in dsl_interface
                assert variable not in variables
                assert call not in calls
                variables.add(variable)
                calls.add(call)
                assert function in dsl_interface or function in variables
                assert args[-1] == ')'
                args = [args[:-1]] if ',' not in args else args[:-1].split(', ')
                for arg in args:
                    assert any([
                        arg in variables, arg in dsl_interface,
                        arg in constants, arg == 'I'
                    ])
            for v in variables:
                assert sum([
                    definition.count(vs) for vs in [
                        f'({v})', f'({v}, ', f', {v})',
                        f', {v}, ', f' {v} = ', f' {v}('
                    ]
                ]) > 1 or v == 'O'
            n_correct += 1
        except:
            print(f'failure: {key}')
            pass
    print(f'{n_correct} out of {n} solvers formatted correctly.')


def test_solvers_correctness(data, solvers_module, benchmark: bool):
    """ tests the implemented solvers for correctness """
    n_correct = 0
    n = len(data["train"])
    for key in data['train'].keys():
        start_time = datetime.datetime.now()
        task = data['train'][key] + data['test'][key]
        try:
            module = importlib.import_module(f"{solvers_module.__name__}.{key}")
            solver = module.solve
            for ex in task:
                assert solver(ex['input']) == ex['output']
            n_correct += 1
        except:
            print(f'failure: {key}', flush=True)
            pass
        if benchmark:
            print(f'{key} {(datetime.datetime.now() - start_time)/ datetime.timedelta(milliseconds=1)}', flush=True)
    print(f'{n_correct} out of {n} tasks solved correctly.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--benchmark', default=False, action='store_true', help='Print timing information for each run')
    args = parser.parse_args()
    data = get_data(train=True)
    run_dsl_tests(dsl, tests)
    test_solvers_formatting(solvers, dsl)
    test_solvers_correctness(data, solvers, args.benchmark)

if __name__ == '__main__':
    main()
