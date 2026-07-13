n=int(input("enter the number"))
lists=[]
while n>0:
    lists.append(n%10)
    n//=10
# print(lists)  
# sorting===========================
num=len(lists)
# print(num)
for i in range(num):
    min_index=i
    for j in range(i+1,num):
        if lists[j]<lists[min_index]:
            min_index=j
    lists[i],lists[min_index]=lists[min_index],lists[i]
print(lists)
sum = 0
for list in range(len(lists)):
    sum = sum*10 + lists[list]
print(sum)
    
        
        
    

