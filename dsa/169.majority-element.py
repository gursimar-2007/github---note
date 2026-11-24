#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        freq=0
        ans=0
        n=len(nums)
        for i in range(0,n):
            if(ans==nums[i]):
                freq+=1
            else:
                freq-=1
        return ans
            
        
# @lc code=end

