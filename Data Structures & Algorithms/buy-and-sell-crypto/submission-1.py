class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Alternative is to keep track of minPrice while iterating normally
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            maxProfit = max(maxProfit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
            right += 1
        return maxProfit

            