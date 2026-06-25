# Last updated: 6/25/2026, 9:13:38 AM
from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1,d2=defaultdict(int),defaultdict(int)

        for i in s1:
            d1[i]+=1
        
        l=0
        for r in range(len(s2)):
            if (r-l)== len(s1):
                if d1==d2:
                    return True
                else:
                    d2[s2[l]]-=1
                    l+=1
            d1[s2[r]]
            d2[s2[r]]+=1
        return d1==d2