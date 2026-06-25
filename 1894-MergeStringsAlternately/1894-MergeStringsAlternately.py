# Last updated: 6/25/2026, 9:10:10 AM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=''
        for i in range(max(len(word1),len(word2))):
            if(len(word1)>i and len(word2)>i):
                result=result+word1[i]+word2[i]
            elif(len(word2)>i):
                result+=word2[i]
            else:
                result+=word1[i]
        return result

        