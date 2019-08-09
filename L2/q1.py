n=int(input("enter a positive integer larger than 2:\n"))
x=2
y=0
while x<n:
    if n%x>0:
       x=x+1
       y=1
       continue
    else:
        print(" %d is not a prime number" %n)
        y=0
        break
if y==1:
    print(" %d is a prime number" %n)

    
    
    

    

    

