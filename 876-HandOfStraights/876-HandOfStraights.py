# Last updated: 6/25/2026, 9:12:30 AM
from collections import defaultdict
import heapq
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        d=defaultdict(int)
        m_heap=list(set(hand))
        for n in hand:
            d[n]+=1
        
        heapq.heapify(m_heap)

        while m_heap:
            curr=m_heap[0]

            for i in range(curr,curr+groupSize):
                if i not in d:
                    return False
                
                d[i]-=1
                if d[i]==0:
                    if m_heap[0]!=i:
                        return False
                    heapq.heappop(m_heap)
        return True