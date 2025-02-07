class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse = True)

        dp = [float(inf)] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for amt in range(coin , amount + 1):
                if dp[amt-coin] != float('inf'):
                    dp[amt] = min(dp[amt] , dp[amt-coin]+1)

        return dp[amount] if dp[amount] != float(inf) else -1




















        """
    RECURSION WITH MEMOIZATION
    space -> O(N)
    time -> O(N^2)
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        minCount = float("inf")
        @lru_cache(None)
        def helper(idx, count, target):
            nonlocal minCount
            if target == 0:
                minCount = min(minCount, count)
                return
            
            if idx >= len(coins) or count >= minCount:  # Pruning unnecessary paths
                return

            max_use = target // coins[idx]  # Max times we can use coins[idx]
            
            for use in range(max_use, -1, -1):  # Try max first to minimize count
                helper(idx + 1, count + use, target - coins[idx] * use)


        helper(0 , 0 , amount)
        return minCount if minCount != float('inf') else -1
        """