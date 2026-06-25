# Last updated: 6/25/2026, 9:11:57 AM
from collections import defaultdict
import heapq
class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph=defaultdict(list)
        for source,dest,cost in  connections:
            graph[source].append((dest,cost))
            graph[dest].append((source,cost))
        
        min_heap=[]
        for node,cost in graph[1]:
            heapq.heappush(min_heap,(cost,1,node))
        
        visited=set()
        visited.add(1)
        acc_cost=[]

        while min_heap:
            cost,source,dest=heapq.heappop(min_heap)
            if dest in visited:
                continue
            acc_cost.append(cost)
            visited.add(dest)

            for new_dest,new_cost in graph[dest]:
                if new_dest not in visited:
                    heapq.heappush(min_heap,(new_cost,dest,new_dest))
        
        if len(visited)==n:
            return sum(acc_cost)
        else:
            return -1 

            


