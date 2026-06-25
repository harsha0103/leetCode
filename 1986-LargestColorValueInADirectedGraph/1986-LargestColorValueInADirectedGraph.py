# Last updated: 6/25/2026, 9:10:06 AM
from collections import defaultdict
class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        graph=defaultdict(list)
        for src,dest in edges:
            graph[src].append(dest)
        
        n,res=len(colors),float('-inf')
        arr=[[0]* 26 for i in range(n)]
        visited=set()
        visiting=set()

        for node in range(n):
            res1=self.dfs(graph,node,visiting,visited,colors,arr)
            res=max(res,res1)
        return -1 if res==float('inf') else res
        
    
    def dfs(self,graph,node,visiting,visited,colors,arr):
        if node in visited:
            return 0
        
        if node in visiting:
            return float('inf')
        
        visiting.add(node)

        index=ord(colors[node])-ord('a')
        arr[node][index]=1

        for neighbor in graph[node]:
            if self.dfs(graph,neighbor,visiting,visited,colors,arr)==float('inf'):
                return float('inf')
            for col in range(26):
                arr[node][col]=max(arr[node][col],arr[neighbor][col]+ (1 if col==index else 0))


        visited.add(node)
        visiting.remove(node)

        return max(arr[node])

        