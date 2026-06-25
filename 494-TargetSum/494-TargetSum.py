# Last updated: 6/25/2026, 9:13:54 AM
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        target=abs(target)
        s1=(sum(nums)+target)//2
        s2=(sum(nums)-target)//2
        if s1+s2!=sum(nums):
            return 0
        print(s1,s2)
        subset_sum=(sum(nums)+target)//2
        n=len(nums)
        m=subset_sum
        d=[[0]* (m+1) for i in range(n+1)]
        d[0][0]=1
        for i in range(1,len(nums)+1):
            for j in range(m+1):
                if nums[i-1]<=subset_sum:
                    d[i][j]=d[i-1][j]+d[i-1][j-nums[i-1]]
                else:
                    d[i][j]=d[i-1][j]
        return d[n][m]