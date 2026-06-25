# Last updated: 6/25/2026, 9:15:29 AM
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited=set()
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs(grid,i,j,visited):
                    count+=1
        
        return count
    
    def dfs(self,grid,row,col,visited):
        valid_r= 0<=row<len(grid)
        valid_c= 0<=col<len(grid[0])

        if not valid_r or not valid_c or (row,col) in visited:
            return False
        
        visited.add((row,col))

        if grid[row][col]=='0':
            return False


        self.dfs(grid,row,col+1,visited)
        self.dfs(grid,row-1,col,visited)
        self.dfs(grid,row,col-1,visited)
        self.dfs(grid,row+1,col,visited)

        return True