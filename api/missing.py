lists=[1,2,3,4,5,6,7,9]
n=len(lists)

for i in range(len(lists)):
    large=i
    if lists[i]>lists[large]:
        large= i+1

num=lists[large]
actual_sum=num*(num+1)/2
sum2=0
for i in range(len(lists)):
    sum2=sum2+lists[i]
new=actual_sum-sum2
print(new)