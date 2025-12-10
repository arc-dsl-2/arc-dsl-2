from dsl import *
from constants import *

def solve(I):
    x1 = ofcolor(I, FIVE)
    x2 = mapply(neighbors, x1)
    O = fill(I, ONE, x2)
    return O
