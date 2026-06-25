# Last updated: 6/25/2026, 9:15:01 AM
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        prefix=1
        postfix=1
        for i in nums:
            output.append(prefix)
            prefix*=i
        
        for i in range(len(nums)-1,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]
        return output