class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, tot, cur):
            if (tot == target):
                res.append(cur.copy())
            elif(i < len(nums) and tot < target):
                # do add num
                cur.append(nums[i])
                dfs(i, tot + nums[i], cur)
                # don't add num
                cur.pop()
                dfs(i+1, tot, cur)
        
        dfs(0, 0, [] )
        return res

