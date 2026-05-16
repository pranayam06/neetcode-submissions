class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        last = 0
        res = 0
        hmap = defaultdict(int)
        hmap[last] += 1

        for num in nums:  
            last = last + num 
            # last - sum = k 
            if last - k in hmap:
                res += hmap[last-k] 
            hmap[last]+=1
        
        return res

                        
