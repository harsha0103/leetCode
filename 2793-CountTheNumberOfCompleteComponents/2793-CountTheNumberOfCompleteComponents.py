# Last updated: 6/25/2026, 9:09:48 AM
from collections import defaultdict

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph={}
        for node in range(n):
            graph[node]=[]

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited=set()
        count=0
        for node in graph:
            if node not in visited: 
                node_count,edge=[0],[0]
                self.dfs(visited,graph,node,node_count,edge)
                if node_count[0]*(node_count[0]-1)//2==edge[0]//2:
                    count+=1
        return count
    
    def dfs(self,visited,graph,node,node_count,edge):
        if node not in visited:
            node_count[0]+=1
            visited.add(node)
            for neighbor in graph[node]:
                edge[0]+=1
                if neighbor not in visited:
                    self.dfs(visited,graph,neighbor,node_count,edge)


            