# Last updated: 6/25/2026, 9:14:42 AM
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start,end=0,n
        ans=0

        while start<=end:
            mid=start+(end-start)//2
            res=isBadVersion(mid)
            if res:
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans
        