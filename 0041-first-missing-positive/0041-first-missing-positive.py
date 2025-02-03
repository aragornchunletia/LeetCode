class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        N = len(nums)
        """
        Algorithm: Cyclic Sort (In-place)
        
        Goal:
        - Find the smallest missing positive integer in O(n) time and O(1) space.
        
        Idea:
        - Each number should be at index `num - 1` (if it's in the range [1, N]).
        - Swap numbers into their correct positions using a while loop.
        - After sorting, the first index where `nums[i] != i + 1` is our answer.
        """

        for i in range(N):
            while 1 <= nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1] , nums[i] = nums[i] , nums[nums[i]-1]


        for i in range(N):
            if nums[i] != i + 1:
                return i + 1

        return N + 1