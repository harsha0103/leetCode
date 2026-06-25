# Last updated: 6/25/2026, 9:13:05 AM
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_max,left_min=0,0

        for i in s:
            if i=='(':
                left_max,left_min=left_max+1,left_min+1
            elif i==')':
                left_max,left_min=left_max-1,left_min-1
            else:
                left_max,left_min=left_max+1,left_min-1
            
            if left_max<0:
                return False
            if left_min<0:
                left_min=0
        return left_min==0 