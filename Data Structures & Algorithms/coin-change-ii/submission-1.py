class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(int)
        memo[0] = 1

        for coin in coins: 
            for x in range(coin, amount+1): 
                memo[x] += memo[x-coin] 
    
        return memo[amount]
                
