n=int(input(""))
inis=0
for i in range(0,n):
    for j in range(0,n-i):
        print("*",end="")
    for j in range(0,inis):
        print(" ",end="")
    for j in range(0,n-i):
        print("*",end="")
    inis+=2
    print()
ns=2*(n-2)        
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end="")
    for j in range(0,inis):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    inis-=2
    print()        