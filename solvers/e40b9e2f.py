from dsl import *
from constants import *

def solve(I):
    x1 = objects(I, F, T, T)
    x2 = neighbors(ORIGIN)
    x3 = mapply(neighbors, x2)
    x4 = first(x1)
    x5 = lbind(intersection, x4)
    x6 = compose(size, x5)
    x7 = compose(hmirror, vmirror)
    x8 = x7(x4)
    x9 = lbind(shift, x8)
    x10 = apply(x9, x3)
    x11 = argmax(x10, x6)
    x12 = paint(I, x11)
    x13 = objects(x12, F, T, T)
    x14 = first(x13)
    x15 = compose(vmirror, dmirror)
    x16 = x15(x14)
    x17 = lbind(shift, x16)
    x18 = apply(x17, x3)
    x19 = argmax(x18, x6)
    O = paint(x12, x19)
    return O
