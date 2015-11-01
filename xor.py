from nand import nand
def xor(a, b):
    return nand(nand(a,nand(a,b)),nand(nand(a,b,),b))
