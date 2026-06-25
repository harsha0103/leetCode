# Last updated: 6/25/2026, 9:11:04 AM
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        l,r=0,0
        add=0
        count=0
        while r<len(arr):
            add+=arr[r]

            if (r-l+1)==k:
                if (add/k)>=threshold:
                    count+=1
                add-=arr[l]
                l+=1
            r+=1

        return count 
