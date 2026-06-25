# Last updated: 6/25/2026, 9:14:36 AM
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if(len(pattern) !=len(s.split(" "))):
            return False

        sp={}
        ps={}

        for i in range(len(pattern)):
            if(pattern[i] in sp ):
                if (sp[pattern[i]]!=s.split(" ")[i]):
                    return False
            else:
                sp[pattern[i]]=s.split(" ")[i]
            
            if (s.split(" ")[i] in ps):
                if (ps[s.split(" ")[i]] !=pattern[i]):
                    return False
            else:
                ps[s.split(" ")[i]]=pattern[i]
            
            
            
        return True
        