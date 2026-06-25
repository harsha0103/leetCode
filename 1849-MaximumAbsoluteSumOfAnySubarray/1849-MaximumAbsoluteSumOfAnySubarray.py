# Last updated: 6/25/2026, 9:10:13 AM
class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max=nums[0]
        global_min=nums[0]
        res_max=nums[0]
        res_min=nums[0]

        for num in nums[1:]:
            temp_max= max(num, global_max+num,global_min+num)
            temp_min= min(num, global_max+num,global_min+num)

            global_max=temp_max
            global_min=temp_min
            res_max=max(global_max,res_max)
            res_min=min(global_min,res_min)
            print(res_max,res_min)
        return max(abs(res_min),res_max)
