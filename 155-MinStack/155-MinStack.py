# Last updated: 6/25/2026, 9:15:59 AM
class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        new_min= min(self.min_stack[-1] if len(self.min_stack)>0 else value,value)
        self.min_stack.append(new_min)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()