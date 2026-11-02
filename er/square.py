class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()        
    # n=int(input(""))
    # pattern1(n)
if __name__ == "__main__":
    n = int(input("Enter n: "))
    obj = Solution()
    obj.pattern1(n)