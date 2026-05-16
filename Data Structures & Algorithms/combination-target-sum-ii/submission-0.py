class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        candidates.sort()

        def dfs(cands, cur, total):  
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return

            for i in range(len(cands)):
                if i > 0 and cands[i] == cands[i - 1]:
                    continue
                dfs(cands[i+1:], cur + [cands[i]], total + cands[i])
                
        dfs(candidates, [], 0)
        return res

                    