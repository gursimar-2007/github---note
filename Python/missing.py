def outliner():
    list=[]
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)
    list.append(7)
    list.append(8)
    list.append(9)
    list.append(10)
    list.append(11)
    n=int(input("enter a num"))
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j]==n:
                print(i)
                print(j)
outliner()