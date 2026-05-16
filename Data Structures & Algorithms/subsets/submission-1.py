class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]: 

        res = []

        def dfs(i, cur):
            if i == len(nums):
                res.append(cur.copy()) 
                return
            
            dfs(i+1, cur)
            new = cur.copy()
            new.append(nums[i])
            dfs(i+1, new) 

        
        dfs(0, [])
        return res



        