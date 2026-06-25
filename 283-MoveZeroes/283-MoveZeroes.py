# Last updated: 6/25/2026, 9:14:40 AM
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write=1
        for read in range(1,len(nums)):
            if nums[write-1]!=0:
                nums[write]=nums[read]
                write+=1
            else:
                nums[write-1]=nums[read]
            
        while write<len(nums):
            nums[write]=0
            write+=1
        
