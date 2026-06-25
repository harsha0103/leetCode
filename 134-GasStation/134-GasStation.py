# Last updated: 6/25/2026, 9:16:16 AM
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        index=0
        total=0
        for i in range(len(gas)):
            total+=(gas[i]-cost[i])
            if total<0:
                index=i+1
                total=0
        return index