class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # want to keep track of the max freq for any substring --> hashmap 
        # compare that max value with k at each addition 
        # max calculation of hmap will always be o(1) since its just o(26)
        
        l = 0 
        r = 0 
        hmap = defaultdict(int)
        res = 0
        while (l <= r < len(s)): 
            # add r to the hmap 
            hmap[s[r]] += 1 
            tot = r-l+1 
            while l <= r and (tot - max(hmap.values()) > k): 
                # take out left 
                hmap[s[l]] -= 1
                tot -= 1 
                l += 1 
            res = max(tot, res)
            r += 1
        return res
            
