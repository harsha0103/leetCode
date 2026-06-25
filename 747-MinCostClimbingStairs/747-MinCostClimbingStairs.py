# Last updated: 6/25/2026, 9:12:51 AM
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        d={}
        def dfs(i):

            if i>=len(cost):
                return 0
            
            if i in d:
                return d[i]
            mn=cost[i]+min(dfs(i+1),dfs(i+2))
            d[i]=mn

            return mn
        
        return min(dfs(1),dfs(0))



