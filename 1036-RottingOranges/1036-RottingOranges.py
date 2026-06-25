# Last updated: 6/25/2026, 9:12:03 AM
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=set()
        count=0
        max_distance=0
        fresh_orange=0
        queue= deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                    visited.add((i,j))
                elif grid[i][j]==1:
                    fresh_orange+=1
    
        while queue:
            c_row,c_col,distance= queue.popleft()
            max_distance = max(max_distance, distance)  # Track the max time taken

            visited.add((c_row,c_col))
            deltas=[(1,0),(0,1),(-1,0),(0,-1)]
            for row,col in deltas:
                new_row=row+c_row
                new_col=col+c_col
                if 0<=new_row<len(grid) and 0<= new_col<len(grid[0]) and grid[new_row][new_col]==1 and (new_row,new_col) not in visited:
                    fresh_orange-=1
                    grid[new_row][new_col] = 2  # Mark as rotten

                    queue.append((new_row,new_col,distance+1))
        
        return max_distance if fresh_orange==0 else -1
                


                    

                