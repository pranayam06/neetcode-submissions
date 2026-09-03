class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(i): 
                dp[i] = dp[i] = max(dp[i], j * max(i-j, dp[i-j]))
        print(dp)
        return dp[n]
