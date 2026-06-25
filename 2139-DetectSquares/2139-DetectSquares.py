# Last updated: 6/25/2026, 9:09:55 AM
from collections import defaultdict
class DetectSquares(object):

    def __init__(self):
        self.arr=[]
        self.points=defaultdict(int)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.points[tuple(point)]+=1
        self.arr.append(tuple(point))
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        px,py=point
        res=0
        
        for x,y in self.arr:
            if abs(x-px)==abs(y-py) and x!=px and y != py:
                res+= self.points[(x,py)]*self.points[(px,y)]
            else:
                continue

        return res 
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)