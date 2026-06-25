# Last updated: 6/25/2026, 9:17:18 AM
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp={}
        def count(r,c,row,col):
            if r==row or c==col:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            if r==row-1 and c==col-1:
                return 1
            
            dp[(r,c)]=count(r+1,c,row,col)+count(r,c+1,row,col)
            return dp[(r,c)]
    
        return count(0,0,m,n)