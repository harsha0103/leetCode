# Last updated: 6/25/2026, 9:18:28 AM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r=0,0
        subset=set()
        max_len=0
        while r<len(s):
            while s[r] in subset:
                subset.remove(s[l])
                l+=1
            max_len=max(max_len,r-l+1)
            subset.add(s[r])
            r+=1


        return max_len