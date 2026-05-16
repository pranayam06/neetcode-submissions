class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(start, end, cur): 
            if end >= len(s) and start == end:
                res.append(cur.copy()) 
                return
            elif end >= len(s):
                return
            elif s[start:end+1] == s[start:end+1][::-1]:
                cur.append(s[start:end+1])
                dfs(end+1, end+1, cur)
                cur.pop() 

            dfs(start, end+1, cur)
        dfs(0,0,[])
        return res
