from xor import xor
def xnor(a, b):
    return nnot(xor(a,b))
print(xnor(0,0))
