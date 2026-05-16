class Solution:
    def maxProfit(self, prices: List[int]) -> int: 

        minbuy = prices[0] 
        prof = 0

        for sell in prices: 
            prof = max (prof, sell - minbuy)
            minbuy = min(minbuy, sell)

        return prof
        


        