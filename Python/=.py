#let a round table with n people and every 3rd person gets eliminated


# n=int(input("enter the number of people on the table"))
lists=[1,2,3,4,5]
skipper=0
# print(f"the length of people on table are{n}")
count=1
for list in lists:
    count+=3
    if count==3:
        lists.remove(3)
                
print(list)
        