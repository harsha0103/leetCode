# Last updated: 6/25/2026, 9:13:04 AM
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)
        par=[ i for i in range(n+1)]
        rank=[1]*(n+1)

        def find(n):
            while n!=par[n]:
                par[n]=par[par[n]]
                n=par[n]
            return n

        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p1]+=rank[p2]
            else:
                par[p2]=p1
                rank[p2]+=rank[p1]
            
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2] 