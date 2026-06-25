# Last updated: 6/25/2026, 9:14:38 AM
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        q=deque()
        grid=rooms
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    q.append((row,col,0))
        
        visited=set()

        while q:
            curr_row,curr_col,distance= q.popleft()
            deltas=[(1,0),(-1,0),(0,-1),(0,1)]
            grid[curr_row][curr_col]=min(distance, grid[curr_row][curr_col])

            for x,y in deltas:
                new_row= curr_row+x
                new_col= curr_col+y

                valid_row= 0<= new_row < len(grid)
                valid_col= 0<= new_col < len(grid[0])
                if valid_row and valid_col and grid[new_row][new_col] !=-1 and (new_row,new_col) not in visited:
                    visited.add((new_row,new_col))
                    q.append((new_row,new_col,distance+1))

