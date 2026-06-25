# Last updated: 6/25/2026, 9:17:39 AM
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]
        candidates.sort()

        def backtrack(i):
            if sum(subset)==target:
                res.append(subset[:])
                return 
            if i>len(candidates)-1 or sum(subset)>target:
                return 
            
            subset.append(candidates[i])
            backtrack(i+1)
            subset.pop()
            while (i+1)< len(candidates) and candidates[i+1]==candidates[i]:
                i=i+1
        

            backtrack(i+1)
        backtrack(0)
        return res