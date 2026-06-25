# Last updated: 6/25/2026, 9:11:39 AM
from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        deltas=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        q=deque([(0,0,0)])
        if grid[0][0]==1:
            return -1
        max_row,max_col=len(grid)-1,len(grid[0])-1
        visited=set()
        while q:
            curr_row,curr_col,dist=q.popleft()
            if (curr_row,curr_col)==(max_row,max_col):
                return dist+1
            
            for x,y in deltas:
                new_row=curr_row + x
                new_col=curr_col + y

                valid_row= 0<= new_row<= max_row
                valid_col= 0<= new_col<= max_col

                if (valid_row and valid_col and (new_row,new_col) not in visited 
                    and grid[new_row][new_col]!=1):
                    visited.add((new_row,new_col))
                    q.append((new_row,new_col,dist+1))
        return -1