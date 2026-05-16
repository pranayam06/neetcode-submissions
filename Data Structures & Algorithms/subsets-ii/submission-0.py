class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(cands, cur):
            res.append(cur.copy())
            for i in range(len(cands)):
                if i > 0 and cands[i] == cands[i-1]:
                    continue
                cur.append(cands[i])
                dfs(cands[i+1:], cur) 
                cur.pop()
                    
        
        dfs(nums, [])
        return res