# Last updated: 6/25/2026, 9:15:21 AM
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph={}
        for c in range(numCourses):
            graph[c]=list()
        
        for c,p in prerequisites:
            graph[c].append(p)
        
        self.path=[]
        visiting,visited=set(),set()
        for c in range(numCourses):
            if not self.dfs(graph,c,visiting,visited):
                return []
        return self.path

    def dfs(self,graph,node,visiting,visited):
        if node in visiting:
            return False
        
        if node in visited:
            return True
        
        visiting.add(node)
        
        for nei in graph[node]:
            if not self.dfs(graph,nei,visiting,visited):
                return False
        
        visiting.remove(node)
        visited.add(node)
        self.path.append(node)

        return True