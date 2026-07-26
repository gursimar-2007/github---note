# n=(input("enter your character"))
# z=0
# for i in range(len(n)):
#     if n[i]=="a" or n[i]=="i" or n[i]=="e" or n[i]=="o" or n[i]=="u":
#         z+=1
#         print(z)
# ==============================================
# n=input("enter your string")
# print(n[::-1])
# list=[1,2,3,4,5,6]
# sum=0
# for i in range(len(list)):
#     sum=sum+list[i]
# print(sum)
# ================================
# list=[1,2,3,4,5]
# max_val=list[0]
# for i in range(len(list)):
#     if list[i]>max_val:
#         max_val=list[i]
# print(max_val)
# ================================
# n=input("enter your number")
# print(len(n))
# for i in range(len(n)-1):
#     print(i)
list=[7,4,6,8,1,5]
n=len(list)
for i in range(n):
    for j in range(n-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list[len(list)-2])