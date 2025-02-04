from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([(0,0)])
        visited = set([0])
        N = len(nums)-1
        while q:
            start , steps = q.popleft()
            visited.add(start)
            if start == N:
                return steps
            for i in range(1 , nums[start]+1):
                nextNode = start + i
                if nextNode not in visited:
                    q.append((nextNode , steps+1))
                    visited.add(nextNode)

        return -1
