# Last updated: 6/25/2026, 9:11:21 AM
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        sarr= sorted(arr)
        d=defaultdict(list)
        m=float('inf')
        for i in range(len(sarr)):
            if (i+1<len(arr)):
                m = min(m,sarr[i+1]-sarr[i])
                d[sarr[i+1]-sarr[i]].append([sarr[i],sarr[i+1] ])
        return d[m]

            
