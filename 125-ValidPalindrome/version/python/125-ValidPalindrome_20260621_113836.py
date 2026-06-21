# Last updated: 6/21/2026, 11:38:36 AM
# Done palindrome check
1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        l,r=0,len(s)-1
8
9        while l<r:
10            if not s[l].isalnum():
11                l+=1
12            elif not s[r].isalnum():
13                r-=1
14            
15            else:
16                if s[l].upper()!=s[r].upper():
17                    return False
18                l+=1
19                r-=1
20        return True
21