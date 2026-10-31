# n=int(input("enter your number"))
n=5
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
        
# def full_pyramid(n):
#     # Outer loop handles the number of rows
#     for i in range(1, n + 1):
#         # Inner loop 1: Prints the leading spaces
#         for j in range(n - i):
#             print(" ", end="")
            
#         # Inner loop 2: Prints the stars (odd sequence: 1, 3, 5, 7...)
#         for k in range(2 * i - 1):
#             print("*", end="")
            
#         # Move to the next line after completing a row
#         print()

# # Generate a pyramid with 5 rows
# full_pyramid(5)
