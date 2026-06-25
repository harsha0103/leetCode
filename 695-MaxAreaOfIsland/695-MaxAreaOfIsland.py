# Last updated: 6/25/2026, 9:13:02 AM
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=set()
        max_count=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count=self.dfs(grid,r,c,visited)
                max_count=max(count,max_count)
        
        return max_count
    
    def dfs(self,grid,row,col,visited):
        valid_r= 0<= row<len(grid) 
        valid_c= 0<= col<len(grid[0])

        if not valid_r or not valid_c:
            return 0
        
        if (row,col) in visited:
            return 0
        
        visited.add((row,col))

        if grid[row][col]==0:
            return 0
        
        temp=(1+self.dfs(grid,row+1,col,visited)+
                self.dfs(grid,row-1,col,visited)+
                self.dfs(grid,row,col+1,visited)+
                self.dfs(grid,row,col-1,visited))
        
        return temp