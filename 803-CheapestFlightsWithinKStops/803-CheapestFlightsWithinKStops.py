# Last updated: 6/25/2026, 9:12:38 AM
from collections import deque
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph=defaultdict(list)

        for source,target,cost in flights:
            graph[source].append((target,cost))
        min_heap=[(0,src,0)]

        best={}
        while min_heap:
            cost, dest,stops=heapq.heappop(min_heap)
            
            if dest==dst:
                return cost

            if dest in best and best[dest]<stops or stops>k:
                continue
            
            best[dest]=stops
            
            for next_stop,inc_cost in graph[dest]:
                heapq.heappush(min_heap,(inc_cost+cost,next_stop,stops+1))
        return -1

        