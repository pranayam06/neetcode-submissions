class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prof = 0
        for i in range(1, len(prices)): 
            if prices[i] < prices[i-1]: 
                res += prof
                prof = 0 
            else: 
                prof += prices[i] - prices[i-1]
        res += prof
        return res

