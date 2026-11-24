#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self,a):
        cur_sum=a[0]
        max_sum=a[0]
        for i in range(1,len(a)):
            cur_sum=max(a[i],cur_sum+a[i])
            max_sum=max(max_sum,cur_sum)
        return max_sum
# @lc code=end

