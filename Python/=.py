lists=[1,2,3,4,5,6,7,8,9,10]
count=1
while len(lists)>1:
    count+=1
    if count==3:
        count=0
        lists.remove(count)
                
print(lists)
        