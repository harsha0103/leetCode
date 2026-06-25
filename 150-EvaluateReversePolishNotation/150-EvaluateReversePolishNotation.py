# Last updated: 6/25/2026, 9:16:04 AM
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        mapping={
            '+': lambda a,b:a+b,
            '-': lambda a,b:a-b,
            '*': lambda a,b:a*b,
            '/': lambda a,b:int(float(a)/b),
        }

        stack=[]
        for i in tokens:
            if i in mapping:
                b=stack.pop()
                a=stack.pop()

                res=mapping[i](a,b)
                stack.append(res)
            else:
                stack.append(int(i))
        res=stack.pop()
        return res