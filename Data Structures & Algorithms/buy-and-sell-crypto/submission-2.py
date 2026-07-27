class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Alternative is to keep track of minPrice while iterating normally
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            profit = price - minPrice
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, profit)
        return maxProfit

            