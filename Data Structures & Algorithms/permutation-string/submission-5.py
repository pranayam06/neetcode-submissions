class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # dont need to rebuild your frequency of each s2 window 

        hmap = Counter(s1)
        l = r = 0
        while (l <= r < len(s2)): 
            while (l < r and hmap[s2[r]] == 0): 
                hmap[s2[l]] += 1  
                l+= 1
                # if still 
            if hmap[s2[r]] == 0: 
                l += 1
                r += 1
            else: 
                hmap[s2[r]] -= 1 
                if r-l+1 == len(s1):  
                    # good str 
                    return True 
                r+= 1
        return False
                
