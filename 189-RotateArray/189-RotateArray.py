# Last updated: 6/25/2026, 9:15:39 AM
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if(k>len(nums)):
            k=k%len(nums)
            #print(k)

        #print(len(nums))
        # Reverse the entire array
        nums.reverse()
        #print(nums)
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        #print(nums)
        # Reverse the rest of the array
        nums[k:] = reversed(nums[k:])
        #print(nums)