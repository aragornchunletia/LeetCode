from typing import List

class Solution:
    """
    Rotating an array by \U0001d458 positions means
    shifting the last \U0001d458 elements to the front while pushing the first 
    N−k elements to the back
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N  # Handle cases where k > N

        def reverse(i, n):
            while i < n:
                nums[i], nums[n] = nums[n], nums[i]
                i += 1
                n -= 1

        reverse(0, N - 1)  # Step 1: Reverse the entire array
        reverse(0, k - 1)  # Step 2: Reverse the first k elements
        reverse(k, N - 1)  # Step 3: Reverse the remaining elements
