# Last updated: 6/25/2026, 9:13:00 AM
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[0]+nums
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            nums[i]=total
        
        for i in range(1,len(nums)):
            if nums[len(nums)-1]-nums[i]==nums[i-1]:
                return i-1
        return -1