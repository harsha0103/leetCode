# Last updated: 6/25/2026, 9:14:52 AM
from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=Counter(nums)

        d1=defaultdict(list)

        for key in d:
            d1[d[key]].append(key)

        return d1[1]
