class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            profit = max(price - buy, profit)
            buy = min(buy, price)
            
        return profit
        