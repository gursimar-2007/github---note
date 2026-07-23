for items in list.pop(0):
    print(items,end="")
for row in list:
    popped_integer = row.pop(3)
    print(popped_integer,end="")
for coloumn in list.reverse():
    print(coloumn)