# Last updated: 6/25/2026, 9:11:48 AM
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        r = ''
        i = 1
        res = str2
        while len(res) >= i:
            candidate = res[:i]
            i += 1
            # Check if candidate divides both str1 and str2 completely
            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:
                if candidate * (len(str1) // len(candidate)) == str1 and candidate * (len(str2) // len(candidate)) == str2:
                    r = candidate
        return r
