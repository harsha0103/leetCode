# Last updated: 6/25/2026, 10:20:35 AM
# binary search for matrix
1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        row,col=len(matrix),len(matrix[0])
9        l,r=0,row*col-1
10
11        while l<=r:
12            mid=(l+r)//2
13            new_r,new_c=mid//col,mid%col
14
15            if matrix[new_r][new_c]==target:
16                return True
17            elif matrix[new_r][new_c]<target:
18                l=mid+1
19            else:
20                r=mid-1
21        return False