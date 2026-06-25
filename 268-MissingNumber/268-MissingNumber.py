# Last updated: 6/25/2026, 9:14:46 AM
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=len(nums)

        for i in range (len(nums)):
            res^=i
            res^=nums[i]

        return res

