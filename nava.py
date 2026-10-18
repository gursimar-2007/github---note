n=int(input("enter your number to check if its a prime number or not"))
if n==2 or n==1:
    print("its a prime number")
for i in range(2,n,1):
    if n%i==0:
        print("its not a prime number")
        break
    else:
        print("its a prime number")
        
