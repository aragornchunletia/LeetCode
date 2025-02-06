from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy, sell, cooldown = -prices[0], 0, 0
        for price in prices:
            buy = max(buy, cooldown - price)
            cooldown = sell
            sell = max(sell, buy + price)
        return sell



        """
        topDown
        space -> O(N) + O(N) callStack
        time -> O(N)
        @lru_cache(None)
        def helper(idx , buy):
            if idx >= len(prices) :
                return 0
            #buy
            if buy == 1:
                return max(-prices[idx] + helper(idx+1,0) , helper(idx+1,buy))
            #sell
            else:
                return max(prices[idx] + helper(idx+2 , 1) , helper(idx+1 , buy))

        return helper(0,1)
        """
        


