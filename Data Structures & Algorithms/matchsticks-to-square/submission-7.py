class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot =sum(matchsticks) 
        dp = {}
        if tot % 4 != 0: 
            return False
        sidelen = tot // 4 
        if max(matchsticks) > sidelen:
            return False

        dp = {}

        def dfs(arr, i):
            state = tuple(sorted(arr))

            if state in dp:
                return dp[state]

            if i == len(matchsticks):
                return True

            for j in range(4):
                if arr[j] + matchsticks[i] <= sidelen:
                    arr[j] += matchsticks[i]

                    if dfs(arr, i + 1):
                        dp[state] = True
                        arr[j] -= matchsticks[i]
                        return True

                    arr[j] -= matchsticks[i]

            dp[state] = False
            return False
        
        return dfs([0,0,0,0], 0)
                 
            