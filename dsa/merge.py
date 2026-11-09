class Solution(object):
    def merge(self, nums1, m, nums2, n,newli):
        newli=[]
        for vals in nums1:
            if(vals==0):
                pass
            else:
                m+=1
                newli.append(vals)
        for vals in nums2:
            if(vals==0):
                pass
            else:
                newli.append(vals)
                n+=1
s1=Solution([1,2,3],[3])

        
        