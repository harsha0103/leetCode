# Last updated: 6/25/2026, 9:12:44 AM
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l,r=0,1

        while l<=r:
            mid=(l+r)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)<target:
                l=mid+1
                r=2*r
            else:
                r=mid-1
        
        return -1