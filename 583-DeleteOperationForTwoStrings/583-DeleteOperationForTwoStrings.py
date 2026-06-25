# Last updated: 6/25/2026, 9:13:32 AM
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n=len(word1)
        m=len(word2)

        d=[[0]*(m+1) for i in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if word1[i-1]==word2[j-1]:
                    d[i][j]=1+d[i-1][j-1]
                else:
                    d[i][j]=max(d[i-1][j],d[i][j-1])
        return n+m-2*d[n][m]