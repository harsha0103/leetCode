# Last updated: 6/25/2026, 9:10:36 AM
class ListNode(object):
    def __init__(self,link='',nxt=None,prev=None):
        self.link=link
        self.next=nxt
        self.prev=prev

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.node=ListNode(homepage)


    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        nde=ListNode(url)
        nxt,prev=None,self.node
        nde.next,nde.prev=nxt,prev
        prev.next=nde
        self.node=self.node.next
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and self.node.prev:
            steps-=1
            self.node=self.node.prev
        return self.node.link


    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and self.node.next:
            self.node=self.node.next
            steps-=1
        return self.node.link


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)