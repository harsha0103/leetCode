# Last updated: 6/25/2026, 9:14:50 AM
from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        visited=set()
        graph=defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        count=0
        if n==1:
            return True
        for node in range(n):
            if node not in visited:
                if self.dfs_traverse(graph,visited,-1,node):
                    return False
                else:
                    count+=1

        return count==1
    
    def dfs_traverse(self,graph,visited,parent,node):
        if node in visited:
            return True        
        visited.add(node)
        for neighbor in graph[node]:
            if parent!=neighbor:
                if self.dfs_traverse(graph,visited,node,neighbor):
                    return True 
 

        return False

