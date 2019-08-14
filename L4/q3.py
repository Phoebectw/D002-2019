n=int(input("please input a positive integer"))
def factorss(n):# your code here
    result = []
    for x in range(1, n + 1):
        if n % x == 0:
            result.append(x)
    return (result)

print(factorss(n))
   
    
