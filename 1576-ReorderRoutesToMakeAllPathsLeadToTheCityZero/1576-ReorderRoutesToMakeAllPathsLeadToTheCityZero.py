# Last updated: 6/25/2026, 9:10:40 AM
from collections import defaultdict 
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph=defaultdict(list)

        for t,s in connections:
            graph[t].append((s,1))
            graph[s].append((t,0))
        
        visited={}
        return self.dfs(graph,0,visited)
    def dfs(self,graph,node,visited):
        if node in visited:
            return visited[node]
        
        visited[node]=0
        for nei,cost in graph[node]:
            if nei not in visited:
                visited[node]+=cost
                visited[node]+=self.dfs(graph,nei,visited)
        return visited[node]
        