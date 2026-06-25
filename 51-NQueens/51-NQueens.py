# Last updated: 6/25/2026, 9:17:26 AM
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board=[['.']*n for _ in range(n)]
        col=set()
        pi=set()
        ni=set()
        res =[]
        def backtrack(r):
            if r==n:
                subset=[''.join(r) for r in board]
                res.append(subset[:])
                return 
            
            for c in range(n):
                if c in col or r+c in pi or r-c in ni or board[r][c]!='.':
                    continue 
                
                board[r][c]='Q'
                pi.add(r+c)
                ni.add(r-c)
                col.add(c)
                backtrack(r+1)
                board[r][c]='.'
                pi.remove(r+c)
                ni.remove(r-c)
                col.remove(c)
        
        backtrack(0)
        return res
