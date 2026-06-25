# Last updated: 6/25/2026, 9:14:29 AM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #buy i+1
        #sell i+2
        dp={}
        def dfs(i,buy):
            if i>=len(prices):
                return 0
            
            if (i,buy) in dp:
                return dp[(i,buy)]
            
            total=float('-inf')
            if buy:
                buying=dfs(i+1,not buy)-prices[i]
                cooldown=dfs(i+1,buy)
                total=max(total,buying,cooldown)
            else:
                sell=dfs(i+2,not buy)+prices[i]
                cooldown=dfs(i+1,buy)
                total=max(total,sell,cooldown)

                
            dp[(i,buy)]=total
            return total
        
        return dfs(0,True)
            