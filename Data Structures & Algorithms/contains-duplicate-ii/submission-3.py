class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = set()

        for i in range(len(nums)):
            if len(hset) > k: 
                hset.remove(nums[i-k-1]) 
            if nums[i] in hset:
                return True 
            hset.add(nums[i])
        return False