# Last updated: 6/25/2026, 9:12:15 AM
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,col=len(grid),len(grid[0])
        visited=set()
        island=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    island=1
                    self.dfs(i,j,visited,grid)
                    break
            if island==1:
                break
        
        visited1=visited.copy()
        q=deque(visited)
        deltas=[(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            curr_r,curr_c,dist=q.popleft()
            
            if grid[curr_r][curr_c]==1 and dist!=0:
                return dist-1
            
            for r,c in deltas:
                new_r,new_c=curr_r+r,curr_c+c

                valid_r=0<=new_r<row
                valid_c=0<=new_c<col

                if valid_r and valid_c and (new_r,new_c,0)  not in visited1:
                    q.append((new_r,new_c,dist+1))
                    visited1.add((new_r,new_c,0))

                



    
    def dfs(self,r,c,visited,grid):
        valid_r=0<= r<len(grid)
        valid_c=0<= c<len(grid[0])

        if not valid_r or not valid_c or (r,c,0) in visited or grid[r][c] ==0:
            return 

        visited.add((r,c,0))

        self.dfs(r+1,c,visited,grid)
        self.dfs(r-1,c,visited,grid)
        self.dfs(r,c+1,visited,grid)
        self.dfs(r,c-1,visited,grid)
