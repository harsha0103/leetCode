# Last updated: 6/25/2026, 9:14:33 AM
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d={}
        # def LIS(nums,i,j):
        #     if i ==len(nums):
        #         return 0
        #     if (i,j) in d:
        #         return d[(i,j)] 
        #     not_take=LIS(i+1,j)
        #     take=0
        #     if j==-1 or nums[j]<nums[i]:
        #         take=1+LIS(i+1,i)
            
        #     res= max(not_take,take)
        #     d[(i,j)]=res
        #     return res
        
        
        # return LIS(0,-1)
        dp=[1]*(len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)

