# Last updated: 6/25/2026, 9:11:13 AM
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d=defaultdict(int)
        for i in arr:
            d[i]+=1
        print(d)
        count=0

        s= set(arr)
        for i in arr:
            if i+1 in s:
                count+=1
        return count
    


        