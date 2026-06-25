# Last updated: 6/25/2026, 9:15:15 AM
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res =[]
        subset=[]

        def backtrack(i):
            if len(subset)==k and sum(subset)==n:
                res.append(subset[:])
                return 
            
            if len(subset)>k or i>9 or sum(subset)>n:
                return 
            
            subset.append(i)
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        backtrack(1)
        return res