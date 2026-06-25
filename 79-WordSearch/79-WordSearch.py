# Last updated: 6/25/2026, 9:17:02 AM
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row,col=len(board),len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    if self.dfs(board,i,j,set(),0,word):
                        return True
        return False
    
    def dfs(self,board,r,c,visited,l,word):
        r_valid= 0<=r<len(board)
        c_valid= 0<= c< len(board[0])

        if not r_valid or not c_valid:
            return False
        if (r,c) in visited:
            return False


        if board[r][c]!=word[l]:
            return False
        visited.add((r,c))
        if l==len(word)-1:
            return True
    
        temp= (self.dfs(board,r+1,c,visited,l+1,word) or 
                self.dfs(board,r-1,c,visited,l+1,word) or
                self.dfs(board,r,c+1,visited,l+1,word) or
                self.dfs(board,r,c-1,visited,l+1,word))
        visited.remove((r,c))
        return temp



