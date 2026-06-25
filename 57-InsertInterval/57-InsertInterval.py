# Last updated: 6/25/2026, 9:17:20 AM
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i:i[0])
        result=[]

        for i in range(len(intervals)):

            if intervals[i][1]<newInterval[0]:
                result.append(intervals[i])
            
            elif newInterval[1]<intervals[i][0]:
                result.append(newInterval)
                return result+intervals[i:]
            else:
                newInterval[0]=min(intervals[i][0],newInterval[0])
                newInterval[1]=max(intervals[i][1],newInterval[1])
        result.append(newInterval)
        return result