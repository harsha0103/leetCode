# Last updated: 6/25/2026, 9:18:32 AM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
     
        d={}
        for i,j in enumerate(nums):
            res=target-j
            if res in d:
                return [d[res],i]
            d[j]=i
        







