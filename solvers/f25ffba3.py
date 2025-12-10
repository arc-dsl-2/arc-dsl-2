from dsl import *
from constants import *

def solve(I):
    x1 = bottomhalf(I)
    x2 = hmirror(x1)
    O = vconcat(x2, x1)
    return O
