#max sum traversal
from heapq import heapify , heappush , heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i : [] for i in range(n)}
        for idx,(a,b) in enumerate(edges):
            adj[a].append((succProb[idx] , b))
            adj[b].append((succProb[idx] , a))

        maxHeap = [(-p,n) for (p , n) in adj[start_node]]
        heapify(maxHeap)
        maxP = 0
        visited = set()
        while maxHeap:
            prob , node = heappop(maxHeap)
            visited.add(node)
            if node == end_node:
                maxP = max(maxP , -prob)

            for p,n in adj[node]:
                if n not in visited:
                    heappush(maxHeap , (prob*p , n))

        return maxP if maxP else 1e-5





        

        

        


        
