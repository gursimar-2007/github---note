def print_number_pattern(n):
    for i in range(1, n + 1):
        # 1. Print increasing sequence from 1 to i
        for j in range(1, i + 1):
            print(j, end="")
        for k in range(2*(n-i)):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()


# Example usage for N = 5
N = 5
print_number_pattern(N)
