# Last updated: 6/25/2026, 9:14:41 AM
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        def dfs(n):
            if n == 0:
                return 0
            if n in dp:
                return dp[n]
            if n < 0:
                return float('inf')
            
            res = float('inf')
            for i in range(1, int(math.sqrt(n)) + 1):
                squr = i * i
                temp = 1 + dfs(n - squr)
                res = min(res, temp)

            dp[n] = res  
            return res

        return dfs(n)
