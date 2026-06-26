# Last updated: 6/26/2026, 3:15:13 PM
# look again at this one
1from collections import defaultdict
2class Solution(object):
3    def characterReplacement(self, s, k):
4        """
5        :type s: str
6        :type k: int
7        :rtype: int
8        """
9        i,j=0,0
10        max_len=0
11        counter=defaultdict(int)
12        while j<len(s):
13            counter[s[j]]+=1
14
15            if j-i+1 - max(counter.values())>k:
16               
17                counter[s[i]]-=1
18                i+=1
19            
20            max_len=max(max_len,j-i+1)
21            j+=1
22        
23        return max_len