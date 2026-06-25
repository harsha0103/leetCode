# Last updated: 6/25/2026, 9:15:13 AM
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l,r=0,0
        new_set=set()
        while r<len(nums):
        
            if nums[r] in new_set:
                return True
            new_set.add(nums[r])

            if (r-l)>=k:
                new_set.remove(nums[l])
                l+=1
            r+=1
        return False