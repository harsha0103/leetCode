# Last updated: 6/25/2026, 9:14:30 AM
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row=len(matrix)
        col=len(matrix[0])
        self.prefix=[[0]*(col+1) for _ in range(row+1)]

        for r in range(1,row+1):
            total=0
            for c in range(1,col+1):
                total+=matrix[r-1][c-1]
                self.prefix[r][c]=total
        
        for c in range(1,col+1):
            total=0
            for r in range(1,row+1):
                total+=self.prefix[r][c]
                self.prefix[r][c]=total
        
 
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        total=self.prefix[row2+1][col2+1]
        up=self.prefix[row1][col2+1]
        left=self.prefix[row2+1][col1]
        dup=self.prefix[row1][col1]

        res=total-up-left+dup
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)