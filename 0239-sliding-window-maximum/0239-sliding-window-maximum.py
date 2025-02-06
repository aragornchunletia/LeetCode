from collections import deque
class Solution:
    """
    Monotonic stack
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque([])

        for i in range(len(nums)):

            # if dq is having idx's which our out of scope for sliding window
            if dq and dq[0] < i - k+1:
                dq.popleft()

            #maintaining a monotonic stack
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            # at k-1 we get our first sliding window
            if i >= k-1:
                res.append(nums[dq[0]])

        return res

            
            

        