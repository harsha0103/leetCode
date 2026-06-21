# Last updated: 6/21/2026, 11:19:08 AM
# row_col check for the valid sudoco
1class Solution(object):
2    def isValidSudoku(self, board):
3        """
4        :type board: List[List[str]]
5        :rtype: bool
6        """
7        for r in range(9):
8            row_set=set()
9            col_set=set()
10            for c in range(9):
11                if (board[r][c] in row_set) or (board[c][r] in col_set):
12                    return False
13                if board[r][c]!='.':
14                    row_set.add(board[r][c])
15                if board[c][r]!='.':
16                    col_set.add(board[c][r])
17
18        for r in range(0,9,3):
19            for c in range(0,9,3):
20                box_set=set()
21                for i in range(3):
22                    for j in range(3):
23                        if board[r+i][c+j] in box_set:
24                            return False
25                        if board[r+i][c+j] !='.':
26                            box_set.add(board[r+i][c+j])
27        return True