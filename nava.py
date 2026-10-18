n=int(input("enter your number for fibbonaci"))
# if n==2 or n==1:
#     print("its a prime number")
# for i in range(2,n,1):
#     if n%i==0:
#         print("its not a prime number")
#         break
#     else:
#         print("its a prime number")
a=0
b=1
print(a,b,end=" ")
for i in range(0,n,1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
