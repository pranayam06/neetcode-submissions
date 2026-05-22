class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        tot = sum(nums)

        if (tot%2): 
            return False

        tot = tot // 2

        memo = [[-1] * (tot + 1) for _ in range(len(nums) + 1)]

        
        def bt(start, cur): 
            if cur > tot: 
                return False
            if cur == tot: 
                return True
            if start == len(nums): 
                return False 
            else: 
                if memo[start][cur] != -1: 
                    return memo[start][cur]
                val = nums[start] 
                memo[start][cur] = bt(start+1, cur+val) or bt(start+1, cur)
                return memo[start][cur] 
        
        return bt(0,0)




        