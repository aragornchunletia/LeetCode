class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target+1)

        dp[0] = 1

        for tgt in range(1,target+1):
            for num in nums:
                if tgt >= num:
                    dp[tgt] += dp[tgt-num]

        return dp[target]