# Last updated: 6/25/2026, 9:14:01 AM
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda i:i[1])
        count=0
        new=intervals[0]
        for i,j in intervals[1:]:
            if i<new[1]:
                count+=1
            else:
                new=[i,j]
        return count