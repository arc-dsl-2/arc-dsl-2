from dsl import *
from constants import *

def solve(I):
    x1 = vsplit(I, TWO)
    x2 = rbind(hsplit, TWO)
    x3 = mapply(x2, x1)
    O = argmax(x3, numcolors)
    return O
