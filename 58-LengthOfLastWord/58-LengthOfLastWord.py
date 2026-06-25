# Last updated: 6/25/2026, 9:17:19 AM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #return (len(''.join(reversed(s)).split()[0]))
        '''this will create space complexty'''
        #return (len(s.split()[-1]))


        total=0
        for i in range(len(s)):
            if i>0 and s[i]!=' ' and s[i-1]!=' ':
                total+=1
            elif i>0 and  s[i-1]==' 'and s[i]!=' ':
                total=1
            elif i==0 and s[i]!=' ':
                total=1
            
        return total

