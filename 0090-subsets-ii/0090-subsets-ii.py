from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sorting to ensure duplicates are adjacent
        res = []
        
        def helper(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            
            # Include nums[i]
            curr.append(nums[i])
            helper(i + 1, curr)
            curr.pop()
            
            # Skip all duplicate elements
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, curr)
        
        helper(0, [])
        return res
