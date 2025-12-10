from dsl import *
from constants import *

def solve(I):
    x1 = objects(I, T, F, T)
    x2 = apply(outbox, x1)
    x3 = mapply(backdrop, x2)
    O = fill(I, ONE, x3)
    return O
