def duplicater():
    list=[1,2,3,4,5,5]
    duplicate=False
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (list[i]==list[j]):
                duplicate=True
                break
    if (duplicate):
        print("yes")
    else:
        print("no")
duplicater()