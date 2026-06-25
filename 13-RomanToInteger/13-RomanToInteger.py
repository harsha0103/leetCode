# Last updated: 6/25/2026, 9:18:11 AM
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
  
        result =0 
        d =     {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
                }
        s=s.replace("IV",'IIII').replace('IX','VIIII')
        s=s.replace("XC",'LXXXX').replace('CD','CCCC')
        s=s.replace("CM",'DCCCC').replace('XL','XXXX')
        for i in s:
            result+= d[i]
        return result

            