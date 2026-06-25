# Last updated: 6/25/2026, 9:13:41 AM
from collections import deque
class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        q=deque()
        row,col=len(grid),len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j]=='*':
                    q.append((i,j,0))

        visited=set()    
        deltas=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            curr_row,curr_col,dist=q.popleft()
            
            if grid[curr_row][curr_col]=='#':
                return dist
              
            for r,c in deltas:
                new_r,new_c=curr_row+r,curr_col+c
                val_r= 0<=new_r<row
                val_c= 0<=new_c<col

                if val_r and val_c and grid[new_r][new_c]!='X' and (new_r,new_c) not in visited:
                    q.append((new_r,new_c,dist+1))
                    visited.add((new_r,new_c))


            

        return -1