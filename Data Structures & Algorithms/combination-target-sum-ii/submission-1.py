class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = [] 
        candidates.sort()

        def dfs(i, tot, cur): 
            if tot == target:
                res.append(cur.copy())  
                return
            if tot > target or i >= len(candidates):
                return 
            # either add num, skip to end 
            else:
                cur.append(candidates[i])
                dfs(i+1, tot + candidates[i], cur)
                cur.pop()
                idx = i + 1
                while idx < len(candidates) and candidates[idx] == candidates[idx-1]:
                    idx += 1
                dfs(idx, tot, cur)
        
        dfs(0, 0, [])
        return res

            
