# n=int(input("ENTER YOUR NUMBER"))
# temp=n
# temp%10
# count=0
# res=0
# while n%10==0:
#     count+=1
#     n=n//10
# while count>0:
#     print(0,end="")
#     count-=1
# while n>0:
#     remainder=n%10
#     res=res*10+remainder
#     n=n//10
# print(res)
n=int(input("enter the number "))
# temp=n
# githmuthia=0
# while temp>0:
#     remainder=temp%10
#     githmuthia=githmuthia*10+remainder
#     temp=temp//10
# if(githmuthia==n):
#     print("its a pallindrome number")
# else:
#     print("its not a pallindrome number")








#! lets count the digits
count=0
temp=n
sum=0
while n>0:
    rem=n%10
    n=n//10
    sum=sum+rem
    # count+=1
    # print(count)
print(sum)

