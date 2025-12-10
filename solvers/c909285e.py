from dsl import *
from constants import *

def solve(I):
    x1 = leastcolor(I)
    x2 = ofcolor(I, x1)
    O = subgrid(x2, I)
    return O
