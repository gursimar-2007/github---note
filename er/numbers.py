n = int(input("Enter your number: "))

# Initialize the space between the left and right number structures
# Each side takes 2 characters per number (the digit + a space)
space = 2 * (2 * n - 2)

for i in range(1, n + 1):
    # 1. Print Left-Hand Numbers
    for j in range(1, i + 1):
        print(j, end=" ")
        
    # 2. Print Middle Spaces
    for j in range(0, space):
        print(" ", end="")
        
    # 3. Print Right-Hand Numbers (In reverse order)
    # Skipping the duplicate peak number on the last row if needed, 
    # or mirroring perfectly as shown below:
    for j in range(i, 0, -1):
        # Prevent double printing the highest number at the very center row
        if j == n and i == n:
            continue
        print(j, end=" ")
        
    # Move to the next row and decrease the space padding
    print()
    space -= 4
