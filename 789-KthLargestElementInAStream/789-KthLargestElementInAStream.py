# Last updated: 6/25/2026, 9:12:43 AM
import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.my_heap=[]
        for num in nums:
            heapq.heappush(self.my_heap,num)
            if len(self.my_heap)>k:
                heapq.heappop(self.my_heap)
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.my_heap,val)
        if len(self.my_heap)>self.k:
            heapq.heappop(self.my_heap)


        return self.my_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)        res=heapq.heappop(self.my_heap)
