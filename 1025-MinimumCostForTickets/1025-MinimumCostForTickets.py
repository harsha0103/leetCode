# Last updated: 6/25/2026, 9:12:06 AM
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        duration = [1, 7, 30]
        n = len(costs)  # 3 ticket types
        m = max(days)
        days_set = set(days)

        # dp[i][j]: min cost to cover up to day j using tickets up to type i
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0  # no cost on day 0

        for i in range(1, n + 1):  # ticket types 1 to 3
            for j in range(1, m + 1):  # days 1 to max day
                if j not in days_set:
                    # no travel, cost same as previous day
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][max(0, j - duration[k])] + costs[k]
                        for k in range(3))

        return dp[n][m]
