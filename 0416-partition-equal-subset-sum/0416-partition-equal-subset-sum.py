class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2

        dp = [False] * (half + 1)
        dp[0] = True

        
        for num in nums:
            for subSum in range(half , num-1 , -1):
                #either the subSum is already True or subSum-num is True
                dp[subSum] |= dp[subSum-num]

        return dp[-1]


        


