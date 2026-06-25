# Last updated: 6/25/2026, 9:16:57 AM
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        max_height=0

        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                prev_i,prev_h=stack.pop()
                height=prev_h*(i-prev_i)
                max_height=max(max_height,height)
                start=prev_i

            stack.append((start,h))
        
        while stack:
            prev_i,prev_h=stack.pop()
            height=prev_h*(len(heights)-prev_i)
            max_height=max(max_height,height)

        return max_height

