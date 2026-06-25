# Last updated: 6/25/2026, 9:15:54 AM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # generic solution 
        '''
        dict = {}
        
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        max_key=max(dict, key=dict.get)
        return max_key '''
        count = 0 
        majority = 0
        for num in nums:
            if count !=0:
                if majority== num:
                    count+=1
                else:
                    count-=1
            elif count==0:
                majority=num
                count+=1
        print(count)
        return majority
