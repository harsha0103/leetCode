# Last updated: 6/25/2026, 9:12:40 AM
import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        min_heap=[(grid[0][0],0,0)]
        max_x=len(grid)-1
        max_y=len(grid[0])-1
        max_height=0
        visited=set()

        while min_heap:
            height,curr_x,curr_y=heapq.heappop(min_heap)
            max_height=max(height,max_height)
            if (curr_x,curr_y)==(max_x,max_y):
                return max_height

            deltas=[(1,0),(-1,0),(0,1),(0,-1)]

            for x,y in deltas:
                new_x=curr_x+x
                new_y=curr_y+y

                valid_x= 0<= new_x <=max_x
                valid_y= 0<= new_y <=max_y
                
                if valid_x and valid_y and (new_x,new_y) not in visited:
                    visited.add((new_x,new_y))
                    heapq.heappush(min_heap,(grid[new_x][new_y],new_x,new_y))
