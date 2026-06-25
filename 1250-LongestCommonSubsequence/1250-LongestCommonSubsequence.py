# Last updated: 6/25/2026, 9:11:27 AM
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n= len(text1)
        m= len(text2)

        d=[[0]* (m+1) for i in range(n+1)]
        res=""

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    d[i][j]=1+d[i-1][j-1]

                else:
                    d[i][j]=max(d[i-1][j],d[i][j-1])
        return d[n][m]