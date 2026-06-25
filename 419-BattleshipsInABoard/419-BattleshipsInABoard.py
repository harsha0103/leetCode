# Last updated: 6/25/2026, 9:14:03 AM
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        grid=board
        visited=set()
        count=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs_traverse(visited,grid,i,j):
                    count+=1
        return count 
    
    def dfs_traverse(self,visited,grid,i,j):
        row_valid=0<=i<len(grid)
        col_valid=0<=j<len(grid[0])

        if not row_valid or not col_valid:
            return False

        if (i,j) in visited or grid[i][j]=='.':
            return False
        
        visited.add((i,j))

        self.dfs_traverse(visited,grid,i+1,j)
        self.dfs_traverse(visited,grid,i-1,j)
        self.dfs_traverse(visited,grid,i,j+1)
        self.dfs_traverse(visited,grid,i,j-1)

        return True 
