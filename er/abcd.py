n=input("enter your interest")
def sidha(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j),end="")
        print()
def putha(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j),end="")
        print()
if (n=="sidha"):
    sidha(5)
else:
    putha(5)