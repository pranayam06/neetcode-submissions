class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = max(prices) 
        res = 0
        for num in prices: 
            # try selling 
            res = max(num - buy, res)
            buy = min(num, buy)
        return res
                