# Last updated: 6/25/2026, 9:16:53 AM
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]
        nums.sort()

        def backtrack(i):
            if i>len(nums)-1:
                res.append(subset[:])
                return 
            
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i=i+1
            backtrack(i+1)
        
        backtrack(0)
        return res 