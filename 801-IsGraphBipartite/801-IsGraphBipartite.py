# Last updated: 6/25/2026, 9:12:39 AM
from collections import defaultdict
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        two_parts={}
        
        for node in range(len(graph)):
            if node not in two_parts:
                if not self.dfs(node,graph,two_parts,False):
                    return False
        return True
    
    def dfs(self,node,graph,two_parts,current_bool):
        if node in two_parts:
            return current_bool==two_parts[node]

        two_parts[node]=current_bool
        for neighbor in graph[node]:
            if not self.dfs(neighbor,graph,two_parts,not current_bool):
                return False
        
        return True