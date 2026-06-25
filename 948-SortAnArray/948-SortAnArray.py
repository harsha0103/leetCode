# Last updated: 6/25/2026, 9:12:19 AM
from collections import deque
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left_sorted=self.sortArray(nums[:mid])
        right_sorted=self.sortArray(nums[mid:])
        return self.merged(left_sorted,right_sorted)
    
    def merged(self,list1,list2):
        left=deque(list1)
        right=deque(list2)
        merge=[]
        while left and right:
            if left[0]<right[0]:
                merge.append(left.popleft())
            else:
                merge.append(right.popleft())
        merge+=left
        merge+=right
        return merge
