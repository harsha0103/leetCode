# Last updated: 6/25/2026, 9:17:25 AM
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        res_sum=nums[0]
        for i in nums[1:]:
            max_sum= max(i,max_sum+i)
            res_sum= max(res_sum,max_sum)
        return res_sum
