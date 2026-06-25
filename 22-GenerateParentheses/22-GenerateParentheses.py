# Last updated: 6/25/2026, 9:17:57 AM
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        subset=[]
        def backtrack(i,j):
            if i==j==n:
                r=''.join(subset)
                res.append(r)
                return 
            
            if i<n:
                subset.append('(')
                backtrack(i+1,j)
                subset.pop()
            
            if j<i:
                subset.append(')')
                backtrack(i,j+1)
                subset.pop()
            
        backtrack(0,0)
        return res