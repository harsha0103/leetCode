# Last updated: 6/25/2026, 9:17:42 AM
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        subset=[]
        res=[]

        def backtrack(i):
            if sum(subset)==target:
                res.append(subset[:])
                return 
            if sum(subset)>target or i>=len(candidates):
                return 
            
            subset.append(candidates[i])
            backtrack(i)
            subset.pop()
            backtrack(i+1)
            return 

        backtrack(0)
        return res