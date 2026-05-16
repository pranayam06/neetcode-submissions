class Solution:
    def maxProfit(self, prices: List[int]) -> int: 

        l = 0 
        r = 1   
        maxp = 0 

        while r < len(prices):
            if (prices[r] <= prices[l]):
                l = r
            else:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit) 

            r+= 1
        
        return maxp
        
    


        