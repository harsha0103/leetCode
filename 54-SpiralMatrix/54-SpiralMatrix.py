# Last updated: 6/25/2026, 9:17:24 AM
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        deltas=[(0,1),(1,0),(0,-1),(-1,0)]
        visited=set()
        row,col=len(matrix),len(matrix[0])
        visited.add((0,0))
        def dfs(r,c,d):

            res.append(matrix[r][c])
            dr,dc=deltas[d]
            nr,nc=r+dr,c+dc
            if 0<= nr<row and 0<= nc<col and (nr,nc) not in visited:
                visited.add((nr,nc))
                dfs(nr,nc,d)

            else:
                d=(d+1)%4
                dr,dc=deltas[d]
                nr,nc=r+dr,c+dc
                if 0<= nr<row and 0<= nc<col and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    dfs(nr,nc,d)
        dfs(0,0,0)
        return res



