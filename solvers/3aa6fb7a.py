from dsl import *
from constants import *

def solve(I):
    x1 = objects(I, T, F, T)
    x2 = mapply(corners, x1)
    O = underfill(I, ONE, x2)
    return O
