# Last updated: 6/25/2026, 9:11:49 AM
from collections import deque
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
    
        q=deque()
        q.append((0,0,0))
        x,y=abs(x),abs(y)

        visited=set((0,0))


        deltas=[(2,1),(1,2),(-2,1),(2,-1),(1,-2),(-1,2),(-2,-1),(-1,-2)]
        while q:
            curr_x,curr_y,dist=q.popleft()
            if x==curr_x and y==curr_y:
                return dist
            for nx,ny in deltas:
                new_x=nx+curr_x
                new_y=ny+curr_y

                valid_x=-2<= new_x<=x+2
                valid_y=-2<= new_y<=y+2

                if valid_x and valid_y and (new_x,new_y) not in visited:
                    visited.add((new_x,new_y))

                    q.append((new_x,new_y,dist+1))


