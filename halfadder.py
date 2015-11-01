from xor import xor
from aand import aand
def halfadder(a, b):
    return {'c':aand(a,b),'o':xor(a,b)}
