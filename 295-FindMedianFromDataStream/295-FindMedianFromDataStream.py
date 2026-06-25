# Last updated: 6/25/2026, 9:14:35 AM
class MedianFinder(object):

    def __init__(self):
        self.first_heap=[]
        self.second_heap=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.first_heap,num*-1)
        if len(self.first_heap)>len(self.second_heap):
            temp=heapq.heappop(self.first_heap) 
            heapq.heappush(self.second_heap,temp*-1)
        if len(self.second_heap)> len(self.first_heap):
            temp=heapq.heappop(self.second_heap) 
            heapq.heappush(self.first_heap,temp*-1)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.first_heap)>len(self.second_heap):
            return self.first_heap[0]*-1
        elif len(self.first_heap)<len(self.second_heap):
            return self.second_heap[0]
        else:
            avg=float(self.first_heap[0]*-1 +  self.second_heap[0])/2
            return avg

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()