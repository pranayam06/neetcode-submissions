class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False for _ in range(len(nums))]
        nums.sort()
        hmap = {}
        cur = []
        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
            for i in range(len(nums)): 
                if used[i]: 
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue 
                
                cur.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                cur.pop()
            
        dfs()
        return res
            
