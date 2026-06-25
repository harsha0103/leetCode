# Last updated: 6/25/2026, 9:12:10 AM
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res,up,down=1,1,1

        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                down=up+1
                up=1
            elif arr[i-1]<arr[i]:
                up=down+1
                down=1
            
            else:
                up,down=1,1
            
            res=max(res,up,down)

        return res         