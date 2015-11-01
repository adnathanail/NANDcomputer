from fulladder import fulladder
def fourbitcomputer(a,b):
    a = list(a)
    a = [int(i) for i in a]
    b = list(b)
    b = [int(i) for i in b]
    f = []
    f.append(fulladder(a[-1],b[-1],0))
    f.append(fulladder(a[-2],b[-2],f[0]['c']))
    f.append(fulladder(a[-3],b[-3],f[1]['c']))
    f.append(fulladder(a[-4],b[-4],f[2]['c']))
    return [f[3]['c'],f[3]['o'],f[2]['o'],f[1]['o'],f[0]['o']]
out = ""
for i in fourbitcomputer('1010','1111'):
    if i:
        out += '1'
    else:
        out += '0'
