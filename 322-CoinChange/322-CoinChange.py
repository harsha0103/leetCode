# Last updated: 6/25/2026, 9:14:27 AM
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp={}
        def dfs(n):
            if n==0:
                dp[n]=0
                return 0
            
            if n in dp:
                return dp[n]
            if n<0:
                dp[n]=float('inf')
                return float('inf')
            
            res=float('inf')
            for coin in coins:
                temp=1+dfs(n-coin)
                res=min(temp,res)
                dp[n]=res
            return res 
        res=dfs(amount)
        return res if res != float('inf') else -1