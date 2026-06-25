# Last updated: 6/25/2026, 9:10:43 AM
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph={}
        for c in range(numCourses):
            graph[c]=[]
        
        for c,p in prerequisites:
            graph[c].append(p)
        res=[]
        for s,t in queries:
            temp=self.dfs(s,t,graph,set())
            res.append(temp)
        
        return res
    
    def dfs(self,s,t,graph,visiting):
        if s in visiting:
            return False
        
        visiting.add(s)
        if s==t:
            return True

        for nei in graph[s]:
            if nei not in visiting:
                if self.dfs(nei,t,graph,visiting):
                    return True
        
        return False