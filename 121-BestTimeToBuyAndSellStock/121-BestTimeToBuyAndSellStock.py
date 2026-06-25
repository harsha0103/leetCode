# Last updated: 6/25/2026, 9:16:29 AM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        max_profit=0
        for r in range(len(prices)):
            res=prices[r]-prices[l]
            if res<0:
                l=r
            max_profit=max(res,max_profit)
        return max_profit
