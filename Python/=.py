#let a round table with n people and every 3rd person gets eliminated
n=int(input("enter the number of people on the table"))
skipper=0
print(f"the length of people on table are{n}")
count=1
for i in range(1,n+1):
    count+=3
    if count==3:
        count=0
                
print(i)
        