# Last updated: 6/25/2026, 9:16:12 AM
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        wordSet=set(wordDict)
        dp=[False]*(n+1)
        dp[0]=True

        for i in range(n+1):
            for j in range (i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i]=True
        
        return dp[n]