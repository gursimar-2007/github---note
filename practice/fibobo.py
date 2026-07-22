n=input()
length=len(n)
n=int(n)
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum+ (r**length)
    n=n//10
if sum==temp:
    print("yes armstrong")
else:
    print("not an armstrong")

