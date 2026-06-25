# Last updated: 6/25/2026, 9:18:09 AM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for  i in strs[1:]:
            if (prefix != ''):
                while not i.startswith(prefix):
                    #print(i)
                    prefix = prefix[:-1]
            
            elif (prefix ==''):
                return ''
        
        return (prefix)


             




        