# При уч. Анастасии Самуйловой

zn=[]
for x in range(200000001,200000100):
    de=set()
    for d in range(1,round(x**0.5)+1):
        if x%d==0:
            de.add(d)
            de.add(x//d)
    if len(de)>5:
        de=sorted(de)
        p=de[5]*de[1]*de[2]*de[3]*de[4]
        if p<x:
            zn.append(p)
print((zn)[:5])