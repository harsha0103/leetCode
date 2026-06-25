# Last updated: 6/25/2026, 9:13:45 AM
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        self.result = ""
        
        if len(s) < k: return s[::-1]
        else: 
            for itm in [s[i:i+2*k] for i in range(0, len(s), 2*k)]:
                self.result+= itm[k-1::-1]+itm[k:] 
            return self.result
            
                