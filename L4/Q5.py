def printer(secret, opened):
    L=[]
    i = 0
    while i < len(secret):
         if i in opened:
              a=secret[i]
              L.append(a)
         else:
             L.append('_')
         i = i + 1
    print(L)
# Note: you might use print(x, end="") to print x without changing line

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___
