w1=input("enter your first word")
w2=input("enter your second word")
w3=input("enter your third word")
w4=input("enter your forth word")
w5=input("enter your fifth word")
w6=input("enter your sixth word")
w7=input("enter your seventh word")
w8=input("enter your eighth word")
w9=input("enter your nineth word")
w10=input("enter your tenth word")
L=[w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
x=1
while x<=10:
    for w in L:
        if w[0]=="a" or w[0]=="e" or w[0] =="i" or w[0]=="o" or w[0]=="u":
            print(w)
        x=x+1    
            
