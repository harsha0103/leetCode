# Last updated: 6/26/2026, 2:00:16 PM
# look again
1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        l,r=0,0
8        substr=set()
9        max_len=0
10        while r<len(s):
11            while s[r] in substr:
12                substr.remove(s[l])
13                l+=1
14            
15            max_len=max(max_len,r-l+1)
16            substr.add(s[r])
17            r+=1
18        
19        return max_len