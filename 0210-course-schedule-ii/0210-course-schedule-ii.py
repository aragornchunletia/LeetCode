from collections import deque
class Solution:
    """
    Similar to Course Schedule 1
    with a little difference that has multiple neigbhors 

    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {i : [] for i in range(numCourses)}
        inDegree = {i : 0 for i in range(numCourses)}

        for a , b in prerequisites:
            adjList[b].append(a)
            inDegree[a] += 1

        q = deque([vertex for vertex , degree in inDegree.items() if degree == 0])
        res = []

        while q:
            v = q.popleft()
            res.append(v)
            for neigh in adjList[v]:
                if inDegree[neigh] > 0:
                    inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    q.append(neigh)

        return res if len(res) == numCourses else []