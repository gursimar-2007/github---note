class Solution:
    def letter_pattern(self, n: int):
        for i in range(1, n + 1):
            row_chars = []
            
            # 1. Increasing sequence (e.g., A -> B -> C)
            for j in range(i):
                row_chars.append(chr(65 + j))
                
            # 2. Decreasing sequence (e.g., B -> A)
            for j in range(i - 2, -1, -1):
                row_chars.append(chr(65 + j))
                
            # Join the characters and print the line
            print("".join(row_chars))

if __name__ == '__main__':
    n = int(input("Enter N: "))
    obj = Solution()
    obj.letter_pattern(n)
