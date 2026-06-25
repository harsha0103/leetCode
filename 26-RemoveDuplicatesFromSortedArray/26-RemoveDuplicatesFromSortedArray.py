# Last updated: 6/25/2026, 9:17:51 AM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=1
        for r in range(1,len(nums)):
            if nums[l-1]!=nums[r]:
                nums[l]=nums[r]
                l+=1
        
        return l


