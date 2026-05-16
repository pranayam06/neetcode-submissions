class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        hs = set(nums)
        print(hs)
        return len(hs) != len(nums)
         