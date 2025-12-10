from dsl import *
from constants import *

def solve(I):
    x1 = objects(I, T, F, T)
    x2 = fork(difference, toindices, box)
    x3 = mapply(x2, x1)
    O = fill(I, ZERO, x3)
    return O
