class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: 
            return n-1
        dp = [k for k in range(n+1)]
        for i in range(1,n+1):
            for j in range(i): 
                dp[i] = max(dp[i], dp[i-j]*j)
        print(dp)
        return dp[n]
