# Last updated: 6/25/2026, 9:14:54 AM
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        arr=[0,0,0]
        new_arr=[0,0,0]

        for sub_arr in costs:
            # for i in range(3):
            #     new_arr[i]= sub_arr[i]+ min(arr[:i]+arr[i+1:])
            new_arr[0] = sub_arr[0] + min(arr[1], arr[2])
            new_arr[1] = sub_arr[1] + min(arr[0], arr[2])
            new_arr[2] = sub_arr[2] + min(arr[0], arr[1])
            arr=new_arr[:]
            print(arr)
        
        return min(arr)
