# Last updated: 6/25/2026, 9:13:01 AM
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n= len(nums1)
        m= len(nums2)

        d=[[0]* (m+1) for i in range(n+1)]
        max_value=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    d[i][j]=1+d[i-1][j-1]
                    max_value =max(max_value,d[i][j])
        
        return max_value