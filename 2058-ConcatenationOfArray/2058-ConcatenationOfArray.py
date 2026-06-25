# Last updated: 6/25/2026, 9:09:57 AM
class Solution(object):
    def getConcatenation(self, nums):

        #return nums +nums
        ans=[0]*2*len(nums)
        l=len(nums)

        for i in range(len(nums)):
            ans[i],ans[i+l]=nums[i],nums[i]
        
        return ans
        
