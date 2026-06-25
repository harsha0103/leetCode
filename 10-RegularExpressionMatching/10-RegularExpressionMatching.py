# Last updated: 6/25/2026, 9:18:15 AM
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n,m=len(s),len(p)
        dp={}
        def dfs(i,j):
            if i >=n and j >=m:
                return  True 
            if (i,j) in dp:
                return dp[(i,j)]
            if j>m:
                return False

            match= i<n and j<m and (s[i]==p[j] or p[j]=='.')

            if j+1<m and p[j+1]=='*':
                dp[(i,j)]= (match and dfs(i+1,j)) or dfs(i,j+2)
                return dp[(i,j)]
            
            if match:
                dp[(i,j)]=  dfs(i+1,j+1)
                return dp[(i,j)]
            dp[(i,j)]= False
            return False
        
        return dfs(0,0)