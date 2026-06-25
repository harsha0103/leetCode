# Last updated: 6/25/2026, 9:16:52 AM
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        mapping=set()
        dp={}
        for i in range(1,27):
            mapping.add(str(i))
        

        def dfs(i):

            if i==len(s):
                return 1
            
            if i in dp:
                return dp[i]
            count=0
            if s[i] in mapping:
                count+=dfs(i+1)
            
            if i+1<len(s) and s[i:i+2] in mapping:
                count+=dfs(i+2)
            
            dp[i]=count
            
            return count
        
        return dfs(0)