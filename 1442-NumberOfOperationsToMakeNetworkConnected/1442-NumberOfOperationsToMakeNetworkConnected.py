# Last updated: 6/25/2026, 9:11:05 AM
from collections import defaultdict
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections)<n-1:
            return -1
        graph=defaultdict(list)
        for i in range(n):
            graph[i]
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        count=0
        visited=set()
        for node in range(n):
            if self.dfs(graph,node,visited):
                count+=1

        return count-1
        
            


    def dfs(self,graph,node,visited):
        if node in visited:
            return False

        visited.add(node)
        for nei in graph[node]:
            self.dfs(graph,nei,visited)
        
        return True 