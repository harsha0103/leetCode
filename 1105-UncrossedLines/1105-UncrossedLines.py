# Last updated: 6/25/2026, 9:11:56 AM
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n= len(nums1)
        m= len(nums2)

        d=[[0]* (m+1) for i in range(n+1)]
        res=""

        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    d[i][j]=1+d[i-1][j-1]

                else:
                    d[i][j]=max(d[i-1][j],d[i][j-1])
        print(res)
        return d[n][m]