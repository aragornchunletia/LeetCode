from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def helper(i , expr):

            if i >= len(nums) and expr == target:
                return 1

            if i >= len(nums):
                return 0

            res = 0
            add = helper(i+1 , expr + nums[i])
            sub = helper(i+1 , expr - nums[i])

            return add + sub

        return helper(0,0)