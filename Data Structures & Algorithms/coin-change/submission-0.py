class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        # base case
        dp[0] = 0
        for i in range(1, amount + 1):
            for k in coins:
                if i - k >= 0:
                    dp[i] = min(dp[i - k] + 1, dp[i])
        
        if dp[amount] < sys.maxsize:
            return dp[amount]
        else:
            return -1   