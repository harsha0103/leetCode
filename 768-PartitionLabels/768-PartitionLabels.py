# Last updated: 6/25/2026, 9:12:48 AM
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index={}

        for i in range(len(s)):
            last_index[s[i]]=i
        

        steps=0
        last=0
        res=[]
        for i in range(len(s)):
            last=max(last,last_index[s[i]])
            steps+=1
            if i==last:
                res.append(steps)
                steps=0
        return res