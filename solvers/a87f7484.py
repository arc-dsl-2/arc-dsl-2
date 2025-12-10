from dsl import *
from constants import *

def solve(I):
    x1 = numcolors(I)
    x2 = portrait(I)
    x3 = branch(x2, dmirror, identity)
    x4 = x3(I)
    x5 = decrement(x1)
    x6 = hsplit(x4, x5)
    x7 = rbind(ofcolor, ZERO)
    x8 = apply(x7, x6)
    x9 = leastcommon(x8)
    x10 = matcher(x7, x9)
    x11 = extract(x6, x10)
    O = x3(x11)
    return O
