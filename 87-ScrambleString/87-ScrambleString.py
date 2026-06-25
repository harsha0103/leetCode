# Last updated: 6/25/2026, 9:16:56 AM
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dp={}
        def dfs(s1,s2):
            if (s1, s2) in dp:
                return dp[(s1, s2)]
            if s1==s2:
                dp[(s1, s2)]=True
                return True
            
            if len(s1)!=len(s2):
                dp[(s1, s2)]=False
                return False
            
            # Early pruning: check if character counts match
            if Counter(s1) != Counter(s2):
                dp[(s1, s2)] = False
                return False

            
            for i in range(1,len(s1)):
                if dfs(s1[i:],s2[i:]) and dfs(s1[:i],s2[:i]):
                    dp[(s1, s2)]=True
                    return True
                
                if dfs(s1[i:],s2[:-i]) and dfs(s1[:i],s2[-i:]):
                    dp[(s1, s2)]=True
                    return True
            dp[(s1, s2)]=False
            return False 
        
        return dfs(s1,s2)