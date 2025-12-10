from dsl import *
from constants import *

def solve(I):
    x1 = ofcolor(I, EIGHT)
    x2 = delta(x1)
    O = fill(I, THREE, x2)
    return O
