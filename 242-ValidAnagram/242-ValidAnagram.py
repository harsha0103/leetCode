# Last updated: 6/25/2026, 9:14:59 AM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False 

        arr1=[0]*26
        for i in s:
            arr1[ord(i)-ord('a')]+=1
        for j in t:
            arr1[ord(j)-ord('a')]-=1
        
        for i in arr1:
            if i !=0:
                return False
        return True


    
