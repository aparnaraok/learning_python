a = {'a':5,'t':3,'c':4,'e':7}
b = {'a':3,'l':9,'e':1,'d':6}

set1 = set(a)

#print(a)

set2 = set(b)

#print(b)

setu = set1.union(set2)
#print(setu)
seti = set1.intersection(set2)
#print(seti)
setdif = setu.symmetric_difference(seti)
#print(setdif)



union={}
for var in setu:
    if a.get(var) and b.get(var):
        union.update({var:[a.get(var),b.get(var)]})
    elif a.get(var):
        d = {var:a.get(var)}
        union.update(d)
    elif b.get(var):
        e = {var:b.get(var)}
        union.update(e)

print("union is",union)

inter = {}
for var in seti:
    if a.get(var):
        d = {var:a.get(var)}
        inter.update(d)
    elif b.get(var):
        e = {var:b.get(var)}
        inter.update(e)

print("intersectios is",inter)

diff = {}

for var in setdif:
    if a.get(var):
        d = {var:a.get(var)}
        diff.update(d)
    elif b.get(var):
        e = {var:b.get(var)}
        diff.update(e)

print("symmetric difference is",diff)



