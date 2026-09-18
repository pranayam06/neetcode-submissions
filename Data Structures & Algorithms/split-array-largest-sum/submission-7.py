class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = defaultdict(int)

        def dfs(i, m):
            if (i,m) in dp: 
                return dp[(i,m)]
            if i == len(nums):
                # no groups left, done with all integers 
                # valid answer 
                if m == 0: 
                    return 0 
                return float('inf')
            if m == 0:
                return float('inf')
                
            
            res = float('inf')
            s = 0 
            for j in range(i, n-m+1):
                s += nums[j]
                # create group with i to j
                res = min(res, (max(s, dfs(j+1, m-1))))
            dp[(i,m)] = res
            return res

           
        return dfs(0, k)