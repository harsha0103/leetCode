# Last updated: 6/25/2026, 9:14:47 AM
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        arr=[0]*len(costs[0])
        new_arr=[0]*len(costs[0])

        for sub_arr in costs:
            for i in range(len(arr)):
                new_arr[i]= sub_arr[i]+ min(arr[i+1:]+arr[:i])
            arr=new_arr[:]
            print(arr)
        
        return min(arr)
