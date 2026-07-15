class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        used = [False for _ in range(len(nums))]

        def dfs(): 
            if len(cur) == len(nums): 
                res.append(cur.copy())
            
            for i in range(len(nums)): 
                if used[i]:
                    continue

                cur.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                cur.pop()
        dfs()
        return res
            
        
