from halfadder import halfadder
from oor import oor
def fulladder(a, b, c):
    return {'c':oor(halfadder(a,b)['c'],halfadder(halfadder(a,b)['o'],c)['c']),'o':halfadder(halfadder(a,b)['o'],c)['o']}
