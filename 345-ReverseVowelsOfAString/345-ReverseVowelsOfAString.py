# Last updated: 6/25/2026, 9:14:18 AM
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=list(s)
        n=''

        for i in s:
            if i in 'aeiouAEIOU':
                n+=i
        rn=''.join(reversed(n))
        print(rn)
        j=0
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                l[i]=rn[j]
                j+=1
        
        return ''.join(l)
