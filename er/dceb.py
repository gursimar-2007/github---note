n=int(input("enter you number"))
for i in range(n):
    start_char_code=(65)+(n-1)-i
    # print(chr(start_char_code))
    for j in range(i+1):
        print(chr(start_char_code +j),end="")
    print()
# class Solution:
#     def pattern18(self, n: int) -> None:
#         # Loop through each row from 0 to n-1
#         for i in range(n):
#             # Calculate the starting character for the current row
#             # 'A' corresponds to ASCII 65
#             start_char_code = 65 + (n - 1) - i
            
#             # Print characters from the starting character up to the N-th character
#             for j in range(i + 1):
#                 print(chr(start_char_code + j), end=" ")
            
#             # Move to the next line after finishing the row
#             print()

# if __name__ == '__main__':
#     n = int(input("Enter n: "))
#     obj = Solution()
#     obj.pattern18(n)
