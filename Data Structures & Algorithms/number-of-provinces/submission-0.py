class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visited = set()
        def dfs(i): 
            # visited means some path is already exploring all these connections 
            for j in range(n): 
                if isConnected[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        res = 0
        for k in range(n): 
            if k not in visited: 
                dfs(k)
                res += 1
        return res