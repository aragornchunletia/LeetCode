from collections import deque
class Solution:
    """
    Topological Sort
    indegree -> number of edges pointing towards it
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {i : [] for i in  range(numCourses)}
        indegree = {i : 0 for i in range(numCourses)}

        #create adj list and update indegree
        for a,b in prerequisites:
            adj_list[a].append(b)
            indegree[b] += 1
        #start with node which has zero indegree
        #means it has no incoming edge hence a good starting point
        #can have multiple starting points
        q = deque([node for node , val in indegree.items() if val == 0])
        visit_counter = 0

        while q:
            curr_node = q.pop()
            visit_counter += 1
            for child in adj_list[curr_node]:
                if indegree[child] > 0:
                    indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        return numCourses == visit_counter




        

        



        
        

        