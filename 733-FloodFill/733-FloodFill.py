# Last updated: 6/25/2026, 9:12:59 AM
from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        replace=image[sr][sc]
        q=deque([(sr,sc)])
        visited=set()
        deltas=[(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            r,c=q.popleft()
            if image[r][c]==replace:
                image[r][c]=color
            
            for i,j in deltas:
                nr=r+i
                nc=c+j
                vr,vc=0<=nr<len(image),0<= nc<len(image[0]) 
                if vr and vc and (nr,nc) not in visited and image[nr][nc]==replace:
                    q.append((nr,nc))
                    visited.add((nr,nc))
        return image