# Last updated: 6/25/2026, 9:12:28 AM
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair =[(p,v) for p,v in zip(position,speed)]
        pair.sort()
        stack=[]
        while pair:
            p,s=pair.pop() 
            time= float(target-p)/s
            if stack and stack[-1]>=time:
                continue 
            stack.append(time)
        return len(stack)

        
