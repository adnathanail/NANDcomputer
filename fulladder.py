from xor import xor
from aand import aand
from oor import oor
def fulladder(a, b, c):
    return {'c':oor(aand(a,b),aand(xor(a,b),c)),'s':xor(c,xor(a,b))}
