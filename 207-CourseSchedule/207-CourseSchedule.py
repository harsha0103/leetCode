# Last updated: 6/25/2026, 9:15:24 AM
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph={}

        for i in range (numCourses):
            graph[i]=list()
        
        visiting=set()
        visited =set()

        for p,c in prerequisites:
            graph[p].append(c)
        
        for i in range(numCourses):
            if not self.dfs(visiting,visited,i,graph):
                return False
        return True


        
    def dfs(self,visiting,visited,node,graph):
        if node in visiting:
            return False

        if node in visited:
            return True 
        
        visiting.add(node)
        for nei in graph[node]:
            res=self.dfs(visiting,visited,nei,graph)
            if not res:
                return False

        
        visited.add(node)
        visiting.remove(node)
        return True