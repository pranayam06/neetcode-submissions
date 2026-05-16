class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        vals = set(nums)
        longest = 0

        for val in vals:
            if val - 1 not in vals: 
                length=1 
                while val + length in vals:
                    length += 1
                longest = max(longest, length)
        return longest



        
        