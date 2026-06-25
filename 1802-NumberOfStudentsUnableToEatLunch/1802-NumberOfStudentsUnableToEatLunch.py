# Last updated: 6/25/2026, 9:10:16 AM
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        q= deque(students)
        res=deque(sandwiches)
        c=0

        while q:
            if c!=len(q):
                if res[0]==q[0]:
                    q.popleft()
                    res.popleft()
                    c=0
                else:
                    q.append(q.popleft())
                    c+=1
            else:
                return c 
        return c

        