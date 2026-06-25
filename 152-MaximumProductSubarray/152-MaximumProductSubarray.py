# Last updated: 6/25/2026, 9:16:02 AM
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        global_max=nums[0]
        global_min=nums[0]
        res=nums[0]

        for num in nums[1:]:
            temp_max=max(num,global_max*num,global_min*num)
            temp_min=min(num,global_max*num,global_min*num)

            global_max=temp_max
            global_min=temp_min

            res=max(global_max,res)
        
        return res
