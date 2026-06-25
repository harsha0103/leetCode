# Last updated: 6/25/2026, 9:10:31 AM
class Solution(object):
    def numIdenticalPairs(self, nums):
        leng = len(nums)
        good_pairs= []


        for i in range(leng):
            for j in range(i+1,leng):
                if (nums[i]==nums[j]):
                    good_pairs.append((i,j))
        
        print(good_pairs)
        return len(good_pairs)
        