class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap = defaultdict(int) 
        for char in t: 
            hmap[char] += 1
        res = s
        found = 0

        met = len(hmap.keys())
    
        l = 0 
        r = 0 

        while (l <= r < len(s)): 
            if s[r] in hmap: 
                hmap[s[r]] -= 1 
                if hmap[s[r]] == 0: 
                    met -= 1
            r+=1 
            while l <= r and not met:
                found = 1
                if len(res) > r-l: 
                    res = s[l:r]
                if s[l] in hmap: 
                    hmap[s[l]] += 1
                    if hmap[s[l]] == 1:
                        met += 1
                l+= 1 
        
        
        if found:
            return res
        else: return ""

            
                
            
            

            