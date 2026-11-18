#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
# class Solution(object):
#     def myPow(self, x, n):
#         bf=n
#         if bf<0:
#             x=1/x
#             bf=-bf
#         ans=1.0
#         while (bf>0):
#             if(bf%2==1):
#                 ans*=x
#             x*=x
        
#             bf//=2
#         return ans
class Solution(object):
    def myPow(self, x, n):
        bf = n
        if bf < 0:
            x = 1.0 / x
            bf = -bf
        
        ans = 1.0
        while bf > 0:
            if bf % 2 == 1:
                ans *= x
            x *= x
            bf //= 2
            
        return ans

# @lc code=end

