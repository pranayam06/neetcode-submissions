class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot =sum(matchsticks) 
        if tot % 4 != 0: 
            return False
        sidelen = tot // 4 
        if max(matchsticks) > sidelen:
            return False

        def dfs(arr, i): 
            if i == len(matchsticks): 
                return True
            for j in range(4):
                if arr[j] + matchsticks[i] <= sidelen:
                    arr[j] += matchsticks[i]
                    res = dfs(arr, i+1)
                    arr[j] -= matchsticks[i]
                    if res: 
                        return True 
            return False
        
        return dfs([0,0,0,0], 0)
                 
            