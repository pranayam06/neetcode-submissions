class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0 
            
            cooldown = dfs(i+1, buying)
            if (buying):
                prof = dfs(i+1, not buying) - prices[i]
            else:
                prof = dfs(i+2, not buying) + prices[i] 
            return max(prof, cooldown)
        
        return dfs(0, True)
