class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap = defaultdict(int)
        for char in t: 
            hmap[char] += 1
        res = s
        found = 0
    
        l = 0 
        r = 0 


        while (l <= r < len(s)): 
            if s[r] in hmap: 
                hmap[s[r]] -= 1 
            r+=1 
            while l <= r and all(ct <= 0 for ct in hmap.values()):
                found = 1
                if len(res) > r-l: 
                    res = s[l:r]
                if s[l] in hmap: hmap[s[l]] += 1
                l+= 1 
        
        
        if found:
            return res
        else: return ""

            
                
            
            

            