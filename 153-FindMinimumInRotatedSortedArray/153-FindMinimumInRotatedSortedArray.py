# Last updated: 6/25/2026, 9:16:00 AM
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1
        n=len(nums)
        while l<=r:
            if nums[l]<nums[r]:
                return nums[l]

            mid=(l+r)//2
            hr=(mid+1)%n
            dr=(mid-1+n)%n
            if nums[mid]<=nums[hr] and nums[mid]<= nums[dr]:
                return nums[mid]
            
            elif nums[mid]>=nums[l]:
                l=mid+1
            
            else:
                r=mid-1
        return -1