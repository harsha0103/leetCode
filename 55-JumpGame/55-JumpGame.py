# Last updated: 6/25/2026, 9:17:23 AM
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l,r=0,0

        while r<len(nums)-1:
            far=0
            for i in range(l,r+1):
                far= max(far,i+nums[i])
            
            l=r+1
            r=far
            if l>r:
                return False
        return True 