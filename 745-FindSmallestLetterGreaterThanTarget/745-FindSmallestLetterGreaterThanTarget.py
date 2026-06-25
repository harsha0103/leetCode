# Last updated: 6/25/2026, 9:12:55 AM
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l,r=0,len(letters)-1
        ans=0

        while l<=r:
            mid= (l+r)//2


            if letters[mid]>target:
                r=mid-1
            else:
                l=mid+1
                
        return letters[l%len(letters)] 

                
            