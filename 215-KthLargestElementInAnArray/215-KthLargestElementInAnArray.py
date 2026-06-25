# Last updated: 6/25/2026, 9:15:16 AM
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        my_heap=[]

        for num in nums:
            heapq.heappush(my_heap,num)
        k1=len(nums)-k

        while k1>0:
            heapq.heappop(my_heap)
            k1-=1
        return heapq.heappop(my_heap)