# Last updated: 6/25/2026, 9:14:06 AM
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total=sum(nums)
        if total%2!=0:
            return False
        n=len(nums)
        m=total//2
        dp=[[False]*(m+1) for _ in range(n+1) ]

        dp[0][0]=True
        for i in range(1,n+1):
            for j in range(m+1):
                if j==0:
                    dp[i][j]==True
                if nums[i-1]<=j:
                    dp[i][j]=(dp[i-1][j-nums[i-1]] or dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][m]