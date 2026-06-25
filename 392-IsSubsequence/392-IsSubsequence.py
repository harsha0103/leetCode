# Last updated: 6/25/2026, 9:14:08 AM
class Solution(object):
    def isSubsequence(self, s, t):

        left,right=0,0

        while right<len(t):
            if left< len(s) and s[left]==t[right]:
                left+=1
            right+=1
        
        return left==len(s)

        