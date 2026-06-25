# Last updated: 6/25/2026, 9:13:48 AM
import sys
sys.setrecursionlimit(10000)
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # n=len(coins)
        # m=amount 

        # d=[[0]* (m+1) for i in range(n+1)]
        # d[0][0]=1    
        # for i in range(1,n+1):
        #     for j in range(m+1):
                    
        #         if coins[i-1]>j:
        #             d[i][j]=d[i-1][j]
        #         else:
        #             d[i][j]=d[i-1][j]+d[i][j-coins[i-1]]
        
        # return d[n][m]
        dp={}
        def dfs(n,amount):
            if amount==0:
                return 1
            
            if (n,amount) in dp:
                return dp[(n,amount)]
            if n>=len(coins) or amount<0:
                dp[(n,amount)]=0
                return 0
            total=0
            temp=dfs(n+1,amount)+dfs(n,amount-coins[n])
            total=max(total,temp)
            dp[(n,amount)]=total

            return total
        
        return dfs(0,amount)