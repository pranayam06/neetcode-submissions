class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))] 
        # dp[text2] [text1]

        for i in range(len(text1)): 
            for j in range(len(text2)): 

                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[j][i] = 1
                    else:
                        dp[j][i] = dp[j-1][i-1] + 1
                else:
                    top = dp[j-1][i] if j > 0 else 0
                    left = dp[j][i-1] if i > 0 else 0
                    diag = dp[j-1][i-1] if i > 0 and j > 0 else 0
                    dp[j][i] = max(top, left, diag)
                        
        return dp[len(text2)-1][len(text1)-1]
