list=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
for items in list.pop(0):
    print(items,end="")
for sublist in list:
    print(sublist[-1],end="")
# for reverser in list:
    # print(reverser)
print(list[::-1])

