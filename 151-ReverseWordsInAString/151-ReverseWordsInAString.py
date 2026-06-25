# Last updated: 6/25/2026, 9:16:03 AM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''  r=""
        w=""
        for i in s:
            if i.isalnum and i!=" ":
                w=w+i
            
            if i==" " and w !="":
                r=w+" "+r
                w=""
        r= w+" "+r
        return r.strip()'''

        spl= [spl for spl in s.split(' ') if spl]
        return ' '.join(spl[::-1])