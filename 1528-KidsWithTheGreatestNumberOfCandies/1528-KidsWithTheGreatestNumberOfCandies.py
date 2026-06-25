# Last updated: 6/25/2026, 9:10:49 AM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[False]*len(candies)
        m=max(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=m):
                result[i]=True
        return result
            
