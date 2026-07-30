lists=[1,2,3,4,5,6,7,8,9,10]

count=1
for list in lists:
    count+=1
    if count==3:
        count==0
        lists.remove(3)
                
print(lists)
        