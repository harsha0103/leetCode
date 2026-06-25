# Last updated: 6/25/2026, 9:17:29 AM
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d= defaultdict(list)

        for s in strs:
            arr=[0]*26
            for c in s:
                arr[ord(c)-ord('a')]+=1
            d[tuple(arr)].append(s)

            #d[''.join(sorted(s))].append(s)
        
        return list(d.values())