# Last updated: 6/25/2026, 9:15:58 AM
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1


            
        while l<=r:
            mid= (l+r)//2

            if (mid==0 or nums[mid]>nums[mid-1]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            
            elif nums[mid-1]<nums[mid]<nums[mid+1]:
                l= mid+1
            
            else:
                r=mid-1
        return l+1
        
        