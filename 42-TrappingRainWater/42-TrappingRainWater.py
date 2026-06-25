# Last updated: 6/25/2026, 9:17:40 AM
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        max_left,max_right=height[l],height[r]
        total=0
        while l<=r:
            if max_left<=max_right:
                temp_water=max_left-height[l]
                total+=temp_water if temp_water>0 else 0
                max_left=max(max_left,height[l])
                l+=1
            
            else:
                temp_water=max_right-height[r]
                total+=temp_water if temp_water>0 else 0
                max_right=max(max_right,height[r])
                r-=1
        
        return total
            