list=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
for items in list.pop(0):
    print(items,end=",")
for sublist in list:
    print(sublist[-1],end=",")
last_row=list[-1]
for i in range(len(last_row)-2,-1,-1):
    print(last_row[i],end=",")
list.pop()
for i in range(1,-1,-1):
    print(list[i][0],end=",")
for sublist in list:
    sublist.pop(0)
    sublist.pop()
for item in list.pop(0):
    print(item, end=",")
last_row=list[-1]
for i in range(len(last_row)-1,-1,-1):
    print(last_row[i],end=",")