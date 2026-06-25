# Last updated: 6/25/2026, 9:17:37 AM
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,0
        jumps=0
        while r<len(nums)-1:
            far=0
            for i in range(l,r+1):
                far=max(nums[i]+i,far)

            l=r+1
            r=far
            jumps+=1
            if l>r:
                return False
        return jumps