# Last updated: 6/25/2026, 9:14:17 AM
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d=defaultdict(int)

        for i in nums:
            d[i]+=1
        
        res=[[] for _ in range(len(nums)+1)]

        for key,value in d.items():
            res[value].append(key)
        
        final=[]
        while k>0:
            if len(res[-1])==0:
                res.pop()
            else:
                temp=res[-1].pop()
                final.append(temp)
                k-=1
        return final
        