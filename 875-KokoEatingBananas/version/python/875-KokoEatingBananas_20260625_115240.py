# Last updated: 6/25/2026, 11:52:40 AM
# koko eat my brain
1 
2class Solution(object):
3    def minEatingSpeed(self, piles, h):
4        """
5        :type piles: List[int]
6        :type h: int
7        :rtype: int
8        """
9        l,r=1,max(piles)
10        res=r
11        while l<=r:
12            mid=(l+r)//2
13            hours=0
14            for p in piles:
15                hours+=math.ceil(float(p)/mid)
16            
17            if hours<=h:
18                res=mid
19                r=mid-1
20            else:
21                l=mid+1
22        
23        return res
24
25