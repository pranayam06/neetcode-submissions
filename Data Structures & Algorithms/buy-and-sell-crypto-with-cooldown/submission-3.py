class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {} 
        # pos ('buy', 'sell'), time 

        def dfs(canBuy, day):  
            if day >= len(prices):
                return 0
            if (canBuy, day) in memo:
                return memo[(canBuy, day)]

            wait = dfs(canBuy, day+1)
            if canBuy == 0: 
                # selling
                sell = prices[day] + dfs(1, day + 2)
                memo[(0, day)] = max(sell, wait) 
            else: 
                #buying 
                buy = dfs(0, day+1) - prices[day] 
                memo[(1,day)] = max(buy, wait)
            
            return memo[(canBuy, day)]



        return dfs(1, 0)


        