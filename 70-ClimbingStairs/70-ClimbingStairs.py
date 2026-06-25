# Last updated: 6/25/2026, 9:17:09 AM
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        arr=[1,2]
        i=2
        while i <=n:
            temp=arr[1]
            arr[1]=sum(arr)
            arr[0]=temp
            i+=1
        
        return arr[0]