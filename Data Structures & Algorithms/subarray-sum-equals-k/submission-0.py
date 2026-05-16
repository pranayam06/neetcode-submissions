from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmps = defaultdict(int) 
        hmps[0] = 1

        ct = 0 
        last = 0

        for num in nums: 
            last = last + num  
            ct += hmps[last-k]  
            hmps[last] += 1   

        return ct




