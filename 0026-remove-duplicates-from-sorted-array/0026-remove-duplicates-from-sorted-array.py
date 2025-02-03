from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        start = 0

        for curr in range(1, len(nums)):
            if nums[curr] != nums[start]:  
                start += 1
                nums[start] = nums[curr]

        return start + 1
