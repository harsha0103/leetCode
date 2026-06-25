# Last updated: 6/25/2026, 9:18:13 AM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        max_water=0
        while l<r:
            min_height=min(height[l],height[r])
            water=min_height*(r-l)
            max_water =max(max_water,water)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_water
