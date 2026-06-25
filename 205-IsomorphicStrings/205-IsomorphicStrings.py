# Last updated: 6/25/2026, 9:15:26 AM
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st={}
        ts={}
        
        for i in range(len(s)):
            if s[i] in st:
                if (st[s[i]] != t[i]):
                    return False 
            else:
                st[s[i]]=t[i]

            if t[i] in ts:
                
                if (ts[t[i]] != s[i]):
                    return False 
            else:
                ts[t[i]]=s[i]

        return True