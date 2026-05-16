class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: 
        hmap = defaultdict(int)
        l = 0  
        
        r = 0 
        res = False

        while (r < len(nums)):  

            if r > l + k:
                hmap[nums[l]] -= 1
                l+= 1 
            elif (hmap[nums[r]] > 0):
                return True
            else: 
                hmap[nums[r]] += 1
                r+= 1 

        return False

            

        
        