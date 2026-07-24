lists=[]
try:
    for i in range(10):
        nums=int(input("enter your number"))
        lists.append(nums)
    print(lists)
    print(f"the total number of elements are{len(lists)}")
    print(f"the highest number is{max(lists)} and lowest is {min(lists)}")
    total=sum(lists)
    print(f"the sum of numbers are{total}")
    print(f"average is {total/len(lists)}")
    print(f"the reverse order of list is {lists[::-1]}")
except ValueError:
    print("please enter valid number")

