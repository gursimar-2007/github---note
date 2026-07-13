lists=[1,2,3,4,0,0,0,1,1,12]
# max = max(list)
# min = min(list)
# print(min)
# print(max)
# current_max=0
# current_min=0
# for i in range(len(list)):
#     if (list[current_max]<list[i]):
#         current_max=i
#     if (list[current_min]>list[i]):
#         current_min=i
# print(list[current_max])
# print(list[current_min])
# k=0
# other_val=0
# for i in range(len(list)):
#     if(list[i]!=0):
#         list[k]=list[i]
#         k+=1
#         # 😊😊😊🚑😒😂🤣😊❤️😍👌💕😁👍👍
# for i in range(k,len(list)):
#     list[i]=0
# print(list)
k=0
freq_list=None
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if(list[i]==list[j]):
# for list in lists:
#     if k==0:
#         freq_list=list
#         print(freq_list)
#     if list==freq_list:
#         k+=0
#     else:
#         k-=0

            
# print(freq_list)
my_list =[1,2,3,4,5,3,2,2,22,1]

# 1. Track the highest count and the winner
max_count = 0
most_repeated = None

# 2. Check each unique item in the list
for i in range(len(my_list)):
    current_count = my_list(i)
    if current_count > max_count:
        max_count = current_count
        most_repeated =i

print(most_repeated)  




        