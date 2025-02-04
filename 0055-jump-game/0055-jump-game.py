class Solution:
    """
    Start from back and check if we can reach the start,
    an immovable place is either its a zero or it eventually leads to a zero
    """
    def canJump(self, nums: List[int]) -> bool:

        prev = len(nums) - 1
        for i in range(len(nums)-2 , -1 , -1):
            if nums[i] + i >= prev:
                prev = i

        return prev == 0
        
        