# Last updated: 6/25/2026, 9:10:07 AM
class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def tc(mid,lc,rc):
            ls=0
            rs=0
            if mid>lc:
                ls = (mid + (mid - lc) - 1) * lc // 2

            else:
                ls = (mid - 1) * mid // 2 + (lc - mid + 1)
            
            if mid>rc:
                rs = (mid + (mid - rc) - 1) * rc // 2

            else:
                rs = (mid - 1) * mid // 2 + (rc - mid + 1)


            return ls+rs+mid


        left,right=1, maxSum
        result=0
        while left<= right:
            mid= (left+right)//2
            lc= index
            rc= n-index-1
            total_sum= tc(mid,lc,rc)

            if total_sum<=maxSum:
                result=mid
                left=mid+1
            else:
                right=mid-1
        return result 
            