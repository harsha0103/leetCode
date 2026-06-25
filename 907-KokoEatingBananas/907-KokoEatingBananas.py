# Last updated: 6/25/2026, 9:12:24 AM
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l,r=1,max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(float(p)/mid)
         
            if hours>h:
                l=mid+1
            else:
                res=mid
                r=mid-1
        return res
            