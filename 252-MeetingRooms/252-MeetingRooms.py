# Last updated: 6/25/2026, 9:14:56 AM
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key=lambda i:i[0])
        prev=intervals[0]            
        for curr in intervals[1:]:
            if prev[1]>curr[0]:
                return False
            else:
                prev=curr
        return True
            