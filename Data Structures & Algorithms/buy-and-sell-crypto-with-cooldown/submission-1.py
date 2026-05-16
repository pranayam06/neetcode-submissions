class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0  
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if (buying):
                prof = dfs(i+1, not buying) - prices[i]
            else:
                prof = dfs(i+2, not buying) + prices[i] 
            dp[(i, buying)] = max(prof, cooldown)
            return max(prof, cooldown)
        
        return dfs(0, True)
