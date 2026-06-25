# Last updated: 6/25/2026, 9:17:05 AM
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res=[]
        subset=[]
        def backtrack(i):
            if len(subset)==k:
                res.append(subset[:])
                return 
            if i>n or len(subset)>k:
                return 

            subset.append(i)
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        
        backtrack(1)
        return res 