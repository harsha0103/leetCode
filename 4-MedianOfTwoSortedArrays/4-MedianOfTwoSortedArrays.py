# Last updated: 6/25/2026, 9:18:27 AM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a,b=nums1,nums2
        total=len(nums1)+len(nums2)
        half= total//2

        if len(b)<len(a):
            a,b=b,a
        l,r=0,len(a)-1
        while True:
            mid_a=(l+r)//2
            mid_b=half-mid_a-2

            aleft= a[mid_a] if mid_a>=0 else float('-inf')
            aright= a[mid_a+1] if mid_a+1<len(a) else float('inf') 
            bleft= b[mid_b] if mid_b>=0 else float('-inf')
            bright= b[mid_b+1] if mid_b+1<len(b) else float('inf')

            if aleft<=bright and bleft<=aright:
                if total%2:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft)+min(aright,bright))/2.0
            elif aleft>bright:
                r=mid_a-1
            else:
                l=mid_a+1
        