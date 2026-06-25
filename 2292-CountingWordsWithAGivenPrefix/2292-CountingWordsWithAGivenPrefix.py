# Last updated: 6/25/2026, 9:09:52 AM
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        j=0
        for i in words:
            if(i.startswith(pref)):
                j+=1
        return j