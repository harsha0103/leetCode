# Last updated: 6/21/2026, 1:13:53 PM
# two pointer
1class Solution(object):
2    def maxArea(self, height):
3        """
4        :type height: List[int]
5        :rtype: int
6        """
7        l,r=0,len(height)-1
8        max_water=0
9        while l<r:
10            min_height=min(height[l],height[r])
11            water=min_height*(r-l)
12            max_water =max(max_water,water)
13            if height[l]>height[r]:
14                r-=1
15            else:
16                l+=1
17        return max_water
18