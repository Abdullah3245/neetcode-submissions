class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 != c2:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
                else:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
        print(dp)
        return dp[m][n]       