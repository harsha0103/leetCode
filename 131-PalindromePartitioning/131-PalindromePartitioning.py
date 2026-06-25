# Last updated: 6/25/2026, 9:16:20 AM
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res=[]
        subset=[]
        def backtrack(i):
            if i>len(s)-1:
                res.append(subset[:])
                return 
            for j in range(i,len(s)):
                if self.is_pal(i,j,s):
                    subset.append(s[i:j+1])
                    backtrack(j+1)
                    subset.pop()
        
        backtrack(0)
        return res
    def is_pal(self,i,j,s):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True