# Last updated: 6/25/2026, 9:12:09 AM
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
                
        my_heap=[]
        for point in points:
            x,y=point
            dist=sqrt(x*x+y*y)
            heapq.heappush(my_heap,(-dist,x,y))
            while len(my_heap)>k:
                heapq.heappop(my_heap)
            
        res=[]
        while my_heap:
            dist,x,y=heapq.heappop(my_heap)
            res.append([x,y])
        return res