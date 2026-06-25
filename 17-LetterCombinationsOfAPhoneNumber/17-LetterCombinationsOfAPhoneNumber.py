# Last updated: 6/25/2026, 9:18:03 AM
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if len(digits)==0:
            return []
        
        res=[]
        subset=[]
        def backtrack(i):
            if i==len(digits):
                r="".join(subset)
                res.append(r)
                return 
            
            if i>len(digits):
                return
            
            for j in mapping[digits[i]]:
                subset.append(j)
                backtrack(i+1)
                subset.pop()
        
        backtrack(0)
        return res
