lists=[1,2,3,4,5,6,7,8,9,10]
count=1
for index in range(0,len(lists)):
    pass
while len(lists)>1:
    (index + 1) % len(lists)
    count+=1
    if count==3:
        count=0
        lists.pop(2)
print(lists)
        