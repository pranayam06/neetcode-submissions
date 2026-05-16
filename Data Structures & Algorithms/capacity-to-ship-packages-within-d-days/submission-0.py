class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) 
        r = sum(weights) 
        while l < r:
            m = l + (r-l) // 2 
            cur = 0 
            time = 1
            for weight in weights:   
                if cur + weight > m:
                    time += 1 
                    cur = weight 
                else: 
                    cur += weight 
            if time <= days: 
                r = m
            else: 
                l = m+1
        
        return l





         