# Last updated: 6/25/2026, 9:14:04 AM
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pac,atl=set(),set()
        row,col=len(heights),len(heights[0])

        def dfs(r,c,visit,prev_height):
            if ( r==row or c ==col or r<0 or c<0 or prev_height>heights[r][c] or
                (r,c) in visit):
                return 
            
            visit.add((r,c))

            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])

        

        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])

        
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])
        res=[]
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))

        return res
    
