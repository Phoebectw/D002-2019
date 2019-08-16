L=[]
for a in range(0,61):
    for b in range(0,61):
        for c in range(0,61):
            d=60-a-b-c
            if d>-1:
                L.append(a*b+b*c+c*d)
from math import*
print(max(L))
