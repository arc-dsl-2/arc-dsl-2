from dsl import *
from constants import *

def solve(I):
    x1 = tojvec(SIX)
    O = crop(I, x1, THREE_BY_THREE)
    return O
