# Last updated: 6/25/2026, 9:17:35 AM
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(i):
            if i>len(nums)-1:
                return [[]]
            
            res=[]
            perm=backtrack(i+1)

            for p  in perm:
                for j in range(len(p)+1):
                    c=p[:]
                    c.insert(j,nums[i])
                    res.append(c)
            
            return res
        
        return backtrack(0)
