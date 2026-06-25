# Last updated: 6/25/2026, 9:14:02 AM
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        d={}
        max_f=0
        res=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            max_f=max(max_f,d[s[r]])
            if (r-l+1)-max_f>k:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res 



            