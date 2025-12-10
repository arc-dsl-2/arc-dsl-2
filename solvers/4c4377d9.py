from dsl import *
from constants import *

def solve(I):
    x1 = hmirror(I)
    O = vconcat(x1, I)
    return O
