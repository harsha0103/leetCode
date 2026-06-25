# Last updated: 6/25/2026, 9:17:21 AM
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        new=intervals[0]
        result=[]
        for i in range(len(intervals)):
            a,b= intervals[i]

            if new[1]<a:
                result.append(new)
                new=intervals[i]

            elif b<new[0]:
                result.append([a,b])
            
            else:
                new=[min(new[0],a),max(new[1],b)]
        result.append(new)
        return result