from nand import nand
def aand(a,b):
    return nand(nand(a,b),nand(a,b))
