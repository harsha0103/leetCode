# Last updated: 6/21/2026, 11:51:26 AM
# two sum when its sorted
1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4        :type numbers: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        l,r=0,len(numbers)-1
9
10        while l<r:
11            if target-numbers[l]==numbers[r]:
12                return [l+1,r+1]
13            elif target-numbers[l]>numbers[r]:
14                l+=1
15            else:
16                r-=1