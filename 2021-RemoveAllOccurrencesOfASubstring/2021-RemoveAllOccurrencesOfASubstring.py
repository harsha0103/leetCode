# Last updated: 6/25/2026, 9:10:03 AM
class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while True:
            #new_s= s.split(part,1)
            index=s.find(part)
            if index == -1:
                break
            s= s[:index] + s[index+len(part):]
            
        return s
            