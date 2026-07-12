class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0] 
        prof = 0
        for i in range(1, len(prices)):
            if prices[i] < buy: 
                buy = prices[i] 
                prof = 0
            else:
                prof += prices[i] - prices[i-1]
                res = max(res, prof)
        return res
            

                