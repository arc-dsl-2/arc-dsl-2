from dsl import *
from constants import *

def solve(I):
    x1 = frontiers(I)
    x2 = merge(x1)
    O = fill(I, TWO, x2)
    return O
