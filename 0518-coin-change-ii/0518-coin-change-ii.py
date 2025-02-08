class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0]*(amount + 1)
        coins.sort()
        dp[0] = 1
        for coin in coins:
            for amt in range(coin , amount + 1):
                dp[amt] += dp[amt - coin ]

        return dp[amount]




"""
        n = len(coins)
        coins.sort(reverse = True)
        memo = dict()
        def recur(idx , amt):
            if idx >= n or amt < 0:
                return 0

            if (idx,amt) in memo :
                return memo[(idx,amt)]

            if amt == 0:
                return 1

            same_coin = recur(idx , amt - coins[idx])
            diff_coin = recur(idx+1 , amt)
            memo[(idx , amt)] = same_coin + diff_coin
            return memo[(idx , amt)]

        return recur(0,amount)
"""

        