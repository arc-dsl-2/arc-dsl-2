from dsl import *
from constants import *

def solve(I):
    x1 = vmirror(I)
    O = hconcat(I, x1)
    return O
