# Last updated: 6/25/2026, 9:15:33 AM
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1,rob2=0,0

        for i in nums:
            temp= max(rob1+i,rob2)
            rob1=rob2
            rob2=temp
        
        return rob2 