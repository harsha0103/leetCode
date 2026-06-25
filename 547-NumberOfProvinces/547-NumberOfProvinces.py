# Last updated: 6/25/2026, 9:13:43 AM
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        edges=[]
        

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j]==1:
                    edges.append((i+1,j+1))

        par=[i for i in range(len(isConnected)+1)]
        rank=[1] * (len(isConnected)+1)

        def find(n):
            while n!=par[n]:
                par[n]=par[par[n]]
                n=par[n]
            return n
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 
            
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2]=p1
                rank[p1]+=rank[p2]
            
            return 
        
        for n1,n2 in edges:
            union(n1,n2)
        count=0
        for i in range(len(par)):
            if i ==par[i] and i!=0:
                count+=1
        return count



