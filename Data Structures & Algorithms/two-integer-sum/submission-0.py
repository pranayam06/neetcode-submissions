class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hm = {} 
        output = []
        for i in range (0, len(nums)): 
            hm[nums[i]] = i;

        for j in range (0, len(nums)): 
            comp = target - nums[j]
            if comp in hm:
                if (j-hm[comp] != 0):
                    return [j, hm[comp]];

         

        