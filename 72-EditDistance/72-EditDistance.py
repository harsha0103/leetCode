# Last updated: 6/25/2026, 9:17:08 AM
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n= len(word1)
        m= len(word2)
        if word1==word2:
            return 0

        d=[[0]* (m+1) for i in range(n+1)]
        res=""


        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j


        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    d[i][j]=d[i-1][j-1]

                else:
                    d[i][j] = 1 + min(
                        d[i - 1][j],     # delete
                        d[i][j - 1],     # insert
                        d[i - 1][j - 1]  # replace
                    )

        return d[n][m] 