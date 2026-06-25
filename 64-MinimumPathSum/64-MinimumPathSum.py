# Last updated: 6/25/2026, 9:17:16 AM
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,col=len(grid),len(grid[0])
        dp={}
        def dfs(r,c):
            if r==row-1 and c==col-1:
                return grid[r][c] 

            if (r,c) in dp:
                return dp[(r,c)]

            if r>=row or c>=col:
                dp[(r,c)]=float('inf')
                return float('inf')

        
            res=grid[r][c]+min(dfs(r+1,c),dfs(r,c+1))
            dp[(r,c)]=res 
            return res
        
        return dfs(0,0)      