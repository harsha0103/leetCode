# Last updated: 6/25/2026, 9:13:11 AM
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        arr=Counter(tasks)
        my_heap=[-freq for freq in arr.values()]

        heapq.heapify(my_heap)

        run_time=0
        q=deque()

        while my_heap or q:
            run_time+=1
            if my_heap:
                freq=1+heapq.heappop(my_heap)
                if freq:
                    q.append((freq,run_time+n))
            
            if q and q[0][1]==run_time:
                heapq.heappush(my_heap,q.popleft()[0])
            
        return run_time