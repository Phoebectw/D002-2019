y=0
b=-999
n= [-120, 14, 93, 320, 1, -999]
print n
while y<6:
    for N in n:
        if N>b:
            b=N
    y=y+1
print ("the largest number is"),( b)    

