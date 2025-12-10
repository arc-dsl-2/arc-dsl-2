from dsl import *
from constants import *

def solve(I):
    x1 = frontiers(I)
    x2 = sfilter(x1, hline)
    x3 = size(x2)
    x4 = positive(x3)
    x5 = branch(x4, identity, dmirror)
    x6 = x5(I)
    x7 = rbind(subgrid, x6)
    x8 = matcher(color, ZERO)
    x9 = compose(flip, x8)
    x10 = partition(x6)
    x11 = sfilter(x10, x9)
    x12 = rbind(ofcolor, ZERO)
    x13 = lbind(mapply, vfrontier)
    x14 = chain(x13, x12, x7)
    x15 = fork(shift, x14, ulcorner)
    x16 = fork(intersection, toindices, x15)
    x17 = mapply(x16, x11)
    x18 = fill(x6, ZERO, x17)
    O = x5(x18)
    return O
