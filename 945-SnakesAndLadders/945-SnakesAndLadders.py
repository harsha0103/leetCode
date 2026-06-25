# Last updated: 6/25/2026, 9:12:20 AM
from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        length=len(board)
        board.reverse()

        def row_col(number):
            row=(number-1)//length
            if row%2==0:
                col=(number-1)%length
            else:
                col=length-(number-1)%length-1
            return (row,col)
        
        q=deque([(1,0)])
        visited=set()
        while q:
            current,distance=q.popleft()

            for i in range(1,7):
                new_number=current+i
                row,col=row_col(new_number)

                
                if board[row][col]!=-1:
                    new_number=board[row][col]
                if new_number==length*length:
                    return distance+1 
                
                if new_number not in visited:
                    visited.add(new_number)
                    q.append((new_number,distance+1))
        return -1