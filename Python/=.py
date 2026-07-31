# lists=[1,2,3,4,5,6,7,8,9,10]
# index=0
# count=1
# while len(lists)>1:
#     count+=1
#     index+=1
#     if count==3:
#         lists.pop(index)
#         count=0
#     else:
#         (index + 1) % len(lists)
# print(lists)
def findTheWinner(n: int, k: int) -> int:
    winner_idx = 0  # Base case: 1 person remaining (0-indexed)
    
    for i in range(2, n + 1):
        winner_idx = (winner_idx + k) % i
        
    return winner_idx + 1  # Convert to 1-indexed for LeetCode
findTheWinner(1,2)
