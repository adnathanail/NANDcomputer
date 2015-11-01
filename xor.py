from nand import nand
from aand import aand
from oor import oor
def xor(a, b):
    return aand(nand(a,b),oor(a,b))
