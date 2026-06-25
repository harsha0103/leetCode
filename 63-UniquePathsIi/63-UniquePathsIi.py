# Last updated: 6/25/2026, 9:17:17 AM
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp={}
        
        def count(r,c,row,col):
            if r==row or c==col:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            if r==row-1 and c==col-1 and obstacleGrid[r][c]==0:
                return 1
            if r==row-1 and c==col-1 and obstacleGrid[r][c]==1:
                return 0
            if obstacleGrid[r][c]==1:
                dp[(r,c)]=0
                return 0
            dp[(r,c)]=count(r+1,c,row,col)+count(r,c+1,row,col)
            return dp[(r,c)]
    
        return count(0,0,len(obstacleGrid),len(obstacleGrid[0]))