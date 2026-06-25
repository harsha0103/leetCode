# Last updated: 6/25/2026, 9:12:56 AM
from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph=defaultdict(list)

        for x,j,t in times:
            graph[x].append((j,t))
        
        min_heap=[(0,k)]
        min_time={}
        total_time=0

        while min_heap:
            curr_time,curr_node= heapq.heappop(min_heap)

            if curr_node in min_time:
                continue
            min_time[curr_node]=curr_time
            total_time=curr_time

            for neighbor,time in graph[curr_node]:
                if neighbor not in min_time:

                    heapq.heappush(min_heap,(curr_time+time,neighbor))
        return total_time if len(min_time)==n else -1