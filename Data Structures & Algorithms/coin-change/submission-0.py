class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1] * (amount+1) 
        memo[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    memo[i] = min(memo[i], 1+ memo[i-c] ) 
        
        if memo[amount] == amount+1:
            return -1
        else:
            return memo[amount]