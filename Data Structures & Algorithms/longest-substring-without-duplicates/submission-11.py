class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  

        seen = dict()
        l = 0 
        res = 0 

        for r in range(len(s)): 
            if s[r] in seen:
                l = max(seen[s[r]]+1, l) 
            res = max(res, r-l+1) 
            seen[s[r]] = r
            
        return res





        