# Last updated: 6/25/2026, 9:17:43 AM
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for r in range(9):
            row_set=set()
            col_set=set()
            for c in range(9):
                if (board[r][c] in row_set) or (board[c][r] in col_set):
                    return False
                if board[r][c]!='.':
                    row_set.add(board[r][c])
                if board[c][r]!='.':
                    col_set.add(board[c][r])

        for r in range(0,9,3):
            for c in range(0,9,3):
                box_set=set()
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] in box_set:
                            return False
                        if board[r+i][c+j] !='.':
                            box_set.add(board[r+i][c+j])
        return True