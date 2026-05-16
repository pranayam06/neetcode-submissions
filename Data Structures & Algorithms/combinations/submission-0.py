class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(num, cur, count): 
            if count == k:
                res.append(cur.copy())
            elif not num == n+1:
                cur.append(num)
                dfs(num+1, cur, count+1)
                cur.pop()
                dfs(num+1, cur, count)
        
        dfs(1, [], 0)
        return res