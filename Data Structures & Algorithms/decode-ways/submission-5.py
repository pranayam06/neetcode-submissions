class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # base case: empty string
        dp[1] = 1  # base case: first character is not '0'

        for i in range(2, n + 1):
            # Single digit decode (if not zero)
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two digit decode (if valid from 10 to 26)
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
            


