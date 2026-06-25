# Last updated: 6/25/2026, 9:10:14 AM
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        malt=0 
        prev=0
        for i in gain:
            prev+=i
            malt=max(malt,prev)
        return malt

        