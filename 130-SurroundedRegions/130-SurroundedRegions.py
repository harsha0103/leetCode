# Last updated: 6/25/2026, 9:16:21 AM
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
    
        row,col=len(board),len(board[0])
        visited=set()
        for r in range(row):
            for c in range(col):
                if (r==0 or r==row-1) and board[r][c]=='O' :
                    self.dfs(r,c,visited,board)
                if (c==0 or c==col-1) and board[r][c]=='O':
                    self.dfs(r,c,visited,board)
        for r in range(row):
            for c in range(col):
                if (r,c) not in visited:
                    board[r][c]='X'

    
    def dfs(self,r,c,visited,board):
        valid_r= 0<= r<len(board)
        valid_c= 0<= c<len(board[0])

        if not valid_r or not valid_c:
            return 
        if (r,c) in visited:
            return 
        if board[r][c]!='O':
            return 
        visited.add((r,c))
        self.dfs(r+1,c,visited,board)
        self.dfs(r-1,c,visited,board)
        self.dfs(r,c-1,visited,board)
        self.dfs(r,c+1,visited,board)


        
            