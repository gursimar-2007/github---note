lists=[1,2,3,4,5,6,7,8,9,10]
index=0
count=1
while len(lists)>1:
    count+=1
    index+=1
    if count==3:
        lists.pop(index)
        count=0
    else:
        (index + 1) % len(lists)
print(lists)
#         people = [...]
# index = ?
# count = 0

# while more than one person remains:
#     count += 1

#     if count == 3:
#         remove the person at index
#         reset count
#     else:
#         move index to the next person (wrap around if needed)