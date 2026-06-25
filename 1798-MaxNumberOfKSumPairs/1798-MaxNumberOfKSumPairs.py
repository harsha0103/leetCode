# Last updated: 6/25/2026, 9:10:19 AM
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        nums.sort()
        left=0
        right=len(nums)-1
        print(nums)

        while left <right:

            total=nums[left]+nums[right]
            if total==k:
                count+=1
                left+=1
                right-=1            
            elif total>k:
                right-=1
            else:
                left+=1
        return count