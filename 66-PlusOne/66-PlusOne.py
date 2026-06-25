# Last updated: 6/25/2026, 9:17:13 AM
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        borrow=1

        for i in range(len(digits)):
            temp=digits[i]+borrow
            digits[i]=temp%10
            borrow=temp//10
        if borrow!=0:
            digits.append(borrow)
        digits.reverse()
        return digits
        
