# Last updated: 6/25/2026, 9:18:01 AM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        arr=[]
        mapping={']':'[', '}':'{',')':'('}

        for i in s: 
            if i =='(' or i=='{' or i=='[':
                arr.append(i)
            else:
                if len(arr)==0:
                    return False
                res=arr.pop()
                if mapping[i]!=res:
                    return False
        return True if len(arr)==0 else False
                    