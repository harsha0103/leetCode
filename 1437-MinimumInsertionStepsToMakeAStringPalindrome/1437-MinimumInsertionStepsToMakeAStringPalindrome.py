# Last updated: 6/25/2026, 9:11:08 AM
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=s
        s2=s[::-1]

        n=len(s)

        d=[[0]*(n+1) for i in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,n+1):

                if s1[i-1]==s2[j-1]:
                    d[i][j]= 1+d[i-1][j-1]
                
                else:
                    d[i][j]=max(d[i][j-1],d[i-1][j])
        
        return n-d[n][n]
