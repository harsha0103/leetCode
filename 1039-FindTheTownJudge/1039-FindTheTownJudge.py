# Last updated: 6/25/2026, 9:12:02 AM
from collections import defaultdict
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        graph=defaultdict(set)
        for i,j in trust:
            graph[i].add(j)
        
        town_judge=-1
        count=0
        for i in range(1,n+1):
            if i not in graph:
                count+=1
                town_judge=i
        
        if count>1:
            return -1
        
        for person in graph:
            if town_judge not in graph[person]:
                return -1
        return town_judge








        

        