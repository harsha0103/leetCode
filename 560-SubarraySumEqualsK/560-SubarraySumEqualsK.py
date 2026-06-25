# Last updated: 6/25/2026, 9:13:40 AM
from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={}
        total=0
        nums=[0]+nums
        res2=0
        for i in nums:
            total+=i
            if total-k in d:
                res2+=d[total-k]
            d[total]=1+d.get(total,0)
        return res2

        