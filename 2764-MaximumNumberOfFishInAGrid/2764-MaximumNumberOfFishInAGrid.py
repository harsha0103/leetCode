# Last updated: 6/25/2026, 9:09:47 AM
class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=set()
        mcount=float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count=self.dfs_traverse(grid,i,j,visited)
                mcount=max(mcount,count)
        return mcount

    def dfs_traverse(self,grid,row,col,visited):
        if (row,col) in visited:
            return 0
        

        valid_row= 0<= row< len(grid) 
        valid_col= 0<= col<len(grid[0])

        if not valid_row or not valid_col:
            return 0 
        
        visited.add((row,col))
        if grid[row][col]==0:
            return 0

        fish=grid[row][col]
        fish+=self.dfs_traverse(grid,row+1,col,visited)
        fish+=self.dfs_traverse(grid,row-1,col,visited)
        fish+=self.dfs_traverse(grid,row,col+1,visited)
        fish+=self.dfs_traverse(grid,row,col-1,visited)

        return fish
