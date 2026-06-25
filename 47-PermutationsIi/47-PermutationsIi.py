# Last updated: 6/25/2026, 9:17:30 AM
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        def backtrack(i):
            if i>=len(nums):
                return [[]]
            
            res =[]


            perm=backtrack(i+1)


            for p in perm:
                for j in range(len(p)+1):
                    c=p[:]
                    c.insert(j,nums[i])
                    
                    res.append(c[:])
            
            return res
        res=backtrack(0)
        res1=set()
        for i in res:
            res1.add(tuple(i))
        
        res2=[]
        for j in res1:
            res2.append(list(j))
        
        return res2