from dsl import *
from constants import *

def solve(I):
    x1 = objects(I, T, F, T)
    x2 = rbind(shoot, DOWN)
    x3 = compose(x2, center)
    x4 = fork(recolor, color, x3)
    x5 = mapply(x4, x1)
    O = paint(I, x5)
    return O
