# n=int(input("enter your number"))
# word="ABCDE"
# for i in range(1,6):
#     for j in range(i):
#         print(word[j],end="")
#     print()
    
# n=int(input("enter your number"))
# word="ABCDE"
# for i in range(5,0,-1):
#     for j in range(i):
#         print(word[j],end=" ")
#     print()
    
n=int(input("enter your number"))
word="ABCDE"
for i in range(5):
    for j in range(i+1):
        print(word[i],end=" ")
    print()
    