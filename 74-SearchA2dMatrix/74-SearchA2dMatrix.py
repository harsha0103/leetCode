# Last updated: 6/25/2026, 9:17:06 AM
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row,col=len(matrix),len(matrix[0])
        l,r= 0, row*col-1

        while l<=r:
            mid=(l+r)//2
            new_row,new_col=mid//col,mid%col

            if matrix[new_row][new_col]>target:
                r=mid-1
            elif matrix[new_row][new_col]<target:
                l=mid+1
            else:
                return True 
        return False

