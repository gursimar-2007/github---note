# for i in range(0,5):
#     for j in range(i):
#         print("*", end=' ')
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end=' ')
#     print()
rows = 7

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1 or i==j or i==j-rows or j==i-rows or :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()