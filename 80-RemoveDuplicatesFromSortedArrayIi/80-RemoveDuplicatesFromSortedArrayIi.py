# Last updated: 6/25/2026, 9:17:01 AM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write=2
        for read in range(2,len(nums)):
            if nums[write-2]!=nums[read]:
                nums[write]=nums[read]
                write+=1
        return write


