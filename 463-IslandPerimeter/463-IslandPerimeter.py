# Last updated: 6/25/2026, 9:13:56 AM
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=set()
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return self.explore(grid,i,j,visited)
        return 0
    
    def explore(self,grid,i,j,visited):
        row_valid= 0<=i<len(grid)
        col_valid= 0<=j<len(grid[0])

        if not row_valid or not col_valid:
            return 1
        
        if grid[i][j]==0:
            return 1
        
        if (i,j) in visited:
            return 0
        
        visited.add((i,j))

        size=0
        size+=self.explore(grid,i-1,j,visited)
        size+=self.explore(grid,i+1,j,visited)
        size+=self.explore(grid,i,j+1,visited)
        size+=self.explore(grid,i,j-1,visited)

        return size 
        