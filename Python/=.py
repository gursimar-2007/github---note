people=[1,2,3,4,5,6,7,8,9]
index=0
count=1
while len(people)>1:
    # index+=1
    count+=1
    if count==3:
        people.pop(index)
        count=0
    else:
         index = (index + 1) % len(people)
print(people[0])
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