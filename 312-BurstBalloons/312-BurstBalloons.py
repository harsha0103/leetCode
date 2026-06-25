# Last updated: 6/25/2026, 9:14:28 AM
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[1]+nums+[1]
        n= len(nums)
        dp=[[-1]*n for _ in range(n)]

        def dfs(nums,i,j):

            if i>=j:
                return 0
            mr=float('-inf')
            if dp[i][j]!=-1:
                return dp[i][j]
            for k in range(i,j):
                temp= dfs(nums,i,k)+dfs(nums,k+1,j)+nums[i-1]*nums[k]*nums[j]
                
                mr=max(mr,temp)
                dp[i][j]=mr

            return mr

        return dfs(nums,1,n-1)