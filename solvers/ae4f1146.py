from dsl import *
from constants import *

def solve(I):
    x1 = objects(I, F, F, T)
    x2 = rbind(colorcount, ONE)
    x3 = argmax(x1, x2)
    O = subgrid(x3, I)
    return O
