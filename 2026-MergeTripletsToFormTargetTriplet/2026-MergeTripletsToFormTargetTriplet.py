# Last updated: 6/25/2026, 9:10:02 AM
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        good_set=set()

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            
            for i in range(3):
                if t[i]==target[i]:
                    good_set.add(i)
            
        return len(good_set)==3