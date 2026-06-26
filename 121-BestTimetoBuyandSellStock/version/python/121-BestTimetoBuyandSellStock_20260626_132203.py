# Last updated: 6/26/2026, 1:22:03 PM
# sliding window
1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        i,j=0,1
8        res=0
9
10        while j<len(prices):
11            total=prices[j]-prices[i]
12            if total<=0:
13                i=j
14            res=max(res,total)
15            j+=1
16
17        return res