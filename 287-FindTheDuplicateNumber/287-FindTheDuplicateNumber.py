# Last updated: 6/25/2026, 9:14:37 AM
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=nums[0]
        fast=nums[0]

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if fast==slow:
                break
        
        head=nums[0]
        while head!=slow:
            slow=nums[slow]
            head=nums[head]
        
        return head