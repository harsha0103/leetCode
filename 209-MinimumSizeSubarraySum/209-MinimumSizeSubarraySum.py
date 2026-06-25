# Last updated: 6/25/2026, 9:15:22 AM
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,0
        total=0
        min_len=float('inf')
        for r in range(len(nums)):
            total+=nums[r]

            while total>= target:
                total-=nums[l]
                min_len=min(min_len,r-l+1)
                l+=1



        return min_len if min_len!=float('inf') else 0
