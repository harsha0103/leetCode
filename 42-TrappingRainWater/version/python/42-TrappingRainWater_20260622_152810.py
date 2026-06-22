# Last updated: 6/22/2026, 3:28:10 PM
# trapping rain water
1class Solution(object):
2    def trap(self, height):
3        """
4        :type height: List[int]
5        :rtype: int
6        """
7        l,r=0,len(height)-1
8        max_left,max_right=height[l],height[r]
9        total=0
10        while l<=r:
11            if max_left<=max_right:
12                temp_water=max_left-height[l]
13                total+=temp_water if temp_water>0 else 0
14                max_left=max(max_left,height[l])
15                l+=1
16            
17            else:
18                temp_water=max_right-height[r]
19                total+=temp_water if temp_water>0 else 0
20                max_right=max(max_right,height[r])
21                r-=1
22        
23        return total
24            