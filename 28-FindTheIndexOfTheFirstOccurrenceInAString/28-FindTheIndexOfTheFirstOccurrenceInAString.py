# Last updated: 6/25/2026, 9:17:49 AM
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        sp= haystack.split(needle)
        return len(sp[0]) if len(sp)>1 else -1
        