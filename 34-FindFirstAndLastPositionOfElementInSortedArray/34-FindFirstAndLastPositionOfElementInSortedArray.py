# Last updated: 6/25/2026, 9:17:46 AM
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=self.left(nums,target)
        right=self.right(nums,target)
        return [left,right]
    
    def left(self,nums,target):
        l,r=0,len(nums)-1
        res=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                res=mid
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return res 

    def right(self,nums,target):
        l,r=0,len(nums)-1
        res=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                res=mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return res 