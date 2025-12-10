from dsl import *
from constants import *

def solve(I):
    x1 = portrait(I)
    x2 = branch(x1, tophalf, lefthalf)
    O = x2(I)
    return O
