# Last updated: 6/25/2026, 9:11:52 AM
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        my_heap=[]
        for num in stones:
            item=(-num,num)
            heapq.heappush(my_heap,item)
        
        while len(my_heap)>1:
            temp1=heapq.heappop(my_heap)[1]
            temp2=heapq.heappop(my_heap)[1]
            res=temp1-temp2
            heapq.heappush(my_heap,(-res,res))
        
        return heapq.heappop(my_heap)[1]