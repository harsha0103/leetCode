# Last updated: 6/25/2026, 9:10:01 AM
from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        i,j=entrance
        visited=set()
        visited.add((i,j))
        q=deque([(i,j,0)])
        deltas=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            row,col,distance=q.popleft()
            

            for i,j in deltas:
                n_row=row+i
                n_col=col+j
                valid_row= 0<= n_row<len(maze)
                valid_col= 0<= n_col<len(maze[0])
                
                if valid_row and valid_col and maze[n_row][n_col]=='.' and (n_row,n_col) not in visited:
                    # Check if it's an exit (boundary cell and not the entrance)
                    if (n_row == 0 or n_row == len(maze) - 1 or n_col == 0 or n_col == len(maze[0]) - 1) and [n_row, n_col] != entrance:
                        return distance + 1
                    q.append((n_row,n_col,distance+1))
                    visited.add((n_row,n_col))
        return -1
        