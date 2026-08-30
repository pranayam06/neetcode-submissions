class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        dp = {}
        def dfs(arr, i):
            t = tuple(set(arr))
            if t in dp:
                return dp[t]
            if i == len(matchsticks): 
                dp[t] = arr[0] == arr[1] == arr[2] == arr[3]
                return dp[t]
            else: 
                copy = arr.copy()
                for j in range(4):
                    arr[j] += matchsticks[i]
                    res = dfs(arr, i+1)
                    arr[j] = copy[j]
                    if res: 
                        dp[t] = True
                        return True 
                dp[t] = False
                return False
        
        return dfs([0,0,0,0], 0)
                 
            