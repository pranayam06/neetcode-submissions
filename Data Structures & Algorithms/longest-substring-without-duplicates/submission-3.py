class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l = 0 
        r = 0 
        seen = {}
        out = 0
        curr = 0

        while (r < len(s)):  
            if s[r] not in seen:
                seen[s[r]] = 1    
                r+=1 
                curr +=1
            else:  
                while (s[r] in seen):
                    seen.pop(s[l]) 
                    l+=1
                    curr -= 1  
            out = max(curr, out)

        return out


            

            

            
        