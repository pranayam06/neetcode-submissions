class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        if tot % k != 0:
            return False 
        nums.sort(reverse=True)
        sub_sum = tot // k
        used = [False for _ in range(len(nums))]



        def dfs(i, k, subset):
            if k == 0: 
                return True 
            if subset == sub_sum: 
                return dfs(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or subset + nums[j] > sub_sum:
                    continue 
                used[j] = True 
                if dfs(j+1, k, subset + nums[j]):
                    return True 
                used[j] = False
            return False
        
        return dfs(0,k, 0)
        
            



