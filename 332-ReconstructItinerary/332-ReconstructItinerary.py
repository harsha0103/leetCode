# Last updated: 6/25/2026, 9:14:22 AM
from collections import defaultdict 
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        itr=defaultdict(list)
        tickets.sort(reverse=True)
        for i,v in tickets:
            itr[i].append(v)
        
        res=[]
        def dfs(src):
            while itr[src]:
                val=itr[src].pop()
                dfs(val)
            res.append(src)

        dfs('JFK')
        
        return res[::-1]
        