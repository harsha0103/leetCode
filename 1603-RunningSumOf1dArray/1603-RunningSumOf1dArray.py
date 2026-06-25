# Last updated: 6/25/2026, 9:10:34 AM
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i]+=nums[i-1] if i>0 else 0
        return nums