from dsl import *
from constants import *

def solve(I):
    x1 = hmirror(I)
    O = vconcat(I, x1)
    return O
