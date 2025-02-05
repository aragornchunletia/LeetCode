class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = max(res[i-2]+nums[i],res[i-1])

        return res[-1]