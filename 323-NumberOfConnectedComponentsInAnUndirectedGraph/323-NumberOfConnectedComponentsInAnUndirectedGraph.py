# Last updated: 6/25/2026, 9:14:26 AM
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        visited=set()

        graph=defaultdict(list)
        for i in range(n):
            graph[i]
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        count=0
        for node in graph:
            if node not in visited:
                self.dfs(graph,visited,node)
                count+=1
        return count
        
    def dfs(self,graph,visited,node):
        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                self.dfs(graph,visited,neighbor)
        return 