# Last updated: 6/25/2026, 9:12:49 AM
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        d=Counter(stones)
        count=0
        for i in jewels:
            if i in d:
                count+=d[i]
        return count