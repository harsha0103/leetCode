# Last updated: 6/25/2026, 9:15:17 AM
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
            
        def dfs(nums):
            rob1,rob2=0,0

            for i in nums:
                temp=max(rob2,rob1+i)
                rob1=rob2
                rob2=temp
            
            return rob2
        
        return max(dfs(nums[1:]),dfs(nums[:-1]))