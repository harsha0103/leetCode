# Last updated: 6/25/2026, 9:12:00 AM
class Solution(object):
    def longestRepeatingSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n= len(s)

        d=[[0]*(n+1) for i in  range(n+1)]
        max_len=0

        for i in range(1,n+1):
            for j in range(1,n+1):
                if i!=j and s[i-1]==s[j-1]:
                    d[i][j]=1+d[i-1][j-1]
                    max_len=max(d[i][j],max_len)

        return max_len        