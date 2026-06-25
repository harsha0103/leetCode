# Last updated: 6/25/2026, 9:14:55 AM
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start=sorted(i[0] for i in intervals)
        end= sorted(i[1] for i in intervals)
        count,max_count=0,0
        i,j=0,0
        while i<len(start):
            if start[i]<end[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            max_count=max(max_count,count)
        return max_count
