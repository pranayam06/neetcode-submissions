class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  
        l = 0 
        freq = defaultdict(int)
        r = 0 
        res = 0
        maxf = 0

        while r < len(s):
            freq[s[r]] += 1
            maxf = max(maxf, freq[s[r]])

            while (r-l + 1) - maxf > k: 
                freq[s[l]]-= 1
                l+=1 
            res = max(res, r-l+1)
            r+=1 
        return res
            
            

        