# Last updated: 6/25/2026, 9:12:34 AM
from collections import defaultdict
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        res=defaultdict(bool)
        visiting=set()

    
        
        for node in range(len(graph)):
            self.dfs(node,graph,visiting,res)
        
        final=[]
        for k,v in res.items():
            if v:
                final.append(k)
        return final
        
    def dfs(self,node,graph,visiting,res):

        if node in visiting:
            return res[node]
            
        visiting.add(node)
        is_safe=True
        for nei in graph[node]:
            if not self.dfs(nei,graph,visiting,res):
                is_safe=False
                
            
            
        res[node]=is_safe
        return res[node]

        