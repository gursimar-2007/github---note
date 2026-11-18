#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, a):
        maxprft=0
        bestbuy=a[0]
        n=len(a)
        for i in range(1,n):
            bestbuy=min(bestbuy,a[i])
            if(a[i]>=bestbuy):
                maxprft=max(maxprft,a[i]-bestbuy)
        return maxprft
            # elif(a[i]<=bestbuy):
                

        
# @lc code=end

