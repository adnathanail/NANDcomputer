from nand import nand
def oor(a,b):
    return nand(nand(a,a),nand(b,b))
