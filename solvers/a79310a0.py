from dsl import *
from constants import *

def solve(I):
    x1 = objects(I, T, F, T)
    x2 = first(x1)
    x3 = move(I, x2, DOWN)
    O = replace(x3, EIGHT, TWO)
    return O
