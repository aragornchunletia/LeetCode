class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for (a,b) , prob in zip(edges , succProb):
            adj[a].append((b,prob))
            adj[b].append((a,prob))

        maxP = [0.0] * n
        maxHeap = [(-1 , start_node)]
        maxP[start_node] = 1.0
        while maxHeap:
            probab , node = heappop(maxHeap)
            probab *= -1
            if node == end_node:
                return probab

            for next_node , p in adj[node]:
                    newProb = p*probab
                    if newProb > maxP[next_node]:
                        maxP[next_node] = newProb
                        heappush(maxHeap,(-newProb , next_node))


        return 1e-5

                
