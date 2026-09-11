class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2: 
            return False 
        target = tot // 2
        seen = set()
        seen.add(0)

        # for each number take a value and try to attain the goal of tot // 2
        for num in nums: 
            for comp in range(target, num-1, -1): 
                if comp - num in seen: 
                    if comp == target: 
                        return True
                    seen.add(comp)
        
        return False                
