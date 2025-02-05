class Solution:
    """
    seems easy but wasnt took the most time for an easy problem
    prefix and suffix problem
    min value from the array at idx i
    max values from the array at idx j 
    where j > i
    """
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0

        for val in prices:
            min_price = min(min_price , val)
            max_profit = max(max_profit , val - min_price)

        return max_profit