class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        tot = sum(nums)

        if (tot%2): 
            return False

        tot = tot // 2
        
        def bt(start, cur): 
            if cur == tot: 
                return True
            if start == len(nums): 
                return False 
            else: 
                val = nums[start]
                if ((val + cur) <= tot): 
                    if bt(start+1, cur+val):
                        return True
                if bt(start+1, cur):
                    return True 
                return False 
        
        return bt(0,0)




        