class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        N = len(prices)
        profit = 0
        l = 0

        for index, sell in enumerate(prices[1:]):
            curr = sell - prices[l]
            if curr < 0:
                print(f"l = {l} and index = {index + 1}")
                l += 1
            if sell < prices[l]:
                print(l)
                l = index + 1
            profit = max(profit, curr)
        
        return profit