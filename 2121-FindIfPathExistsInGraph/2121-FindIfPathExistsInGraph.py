# Last updated: 6/25/2026, 9:09:56 AM
from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph= defaultdict(list)

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited=set()
        if self.dfs(source,graph,visited,destination):
            return True 
        
        return False
    
    def dfs(self,s,graph,visited,d):
        if s==d:
            return True

        if s in visited:
            return False
        visited.add(s)
        for nei in graph[s]:
            if self.dfs(nei,graph,visited,d):
                return True
        
        return False
        