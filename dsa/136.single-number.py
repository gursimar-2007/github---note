#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, a):
        start=0
        end=len(a)-1
        if(len(a)==1):
            return a[0]
        while (start<=end):
            mid=start+(end-start)/2
            if(mid==0 and a[0]!=a[1]):
                return a[start]
                
            if(mid==end-1 and a[end-1]!=a[end-2]):
                return a[end]
                
            if(a[mid-1]!=a[mid] and a[mid+1]!=mid):
                return a[mid]
                
            if(mid%2==0):
                if(a[mid-1]==a[mid]):
                    end=mid-1
                    
                else:
                    start=mid+1
                    
            else:
                if(a[mid-1]==a[mid]):
                    start=mid+1
                    
                else:
                    end=mid-1
                    
        # for i in range(a[i]):
    
# @lc code=end

