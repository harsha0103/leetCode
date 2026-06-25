# Last updated: 6/25/2026, 9:12:58 AM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        res=[0]*len(temperatures)
        for i,v in enumerate(temperatures):
            while stack and stack[-1][1]<v:
                prev_i,prev_v=stack.pop()
                res[prev_i]=i-prev_i
            stack.append((i,v))
        
        return res
            
