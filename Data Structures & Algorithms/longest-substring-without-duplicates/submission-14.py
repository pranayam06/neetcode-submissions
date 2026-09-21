class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        res = 0
        working_set = set()
        while (l <= r < len(s) ): 
            while s[r] in working_set: 
                working_set.remove(s[l]) 
                l+=1
            
            working_set.add(s[r])
            r += 1 
            res = max(res, r-l)
        return res
            
                
