class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        
        max = 0;
        for j in range (0, len(prices)):
            for k in range (j+1, len(prices)): 
                if prices[k] - prices[j] > max: 
                    max = prices[k] - prices[j]


        return max

        