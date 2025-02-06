from typing import List

class Solution:
    """
    Using cycle detection like a LL
    space -> O(1)
    time -> O(N)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]  
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
