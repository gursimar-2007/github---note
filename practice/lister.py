list=[]
N=int(input())



for i in range(N):
    parts = input().split()
    command = parts[0]

    if command == "insert":
        index = int(parts[1])
        element = int(parts[2])
        list.insert(index, element)

    elif command == "print":
        print(list)

    elif command == "remove":
        element = int(parts[1])
        list.remove(element)

    elif command == "append":
        element = int(parts[1])
        list.append(element)

    elif command == "sort":
        list.sort()

    elif command == "pop":
        list.pop()

    elif command == "reverse":
        list.reverse()