class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        hset = set()
        res = 0
        l = 0 
        r = 0 
        while (l<=r and r<len(s)):
            if (s[r] not in hset):
                hset.add(s[r])
                r+=1
                res = max(res, r-l)

            else:
                hset.remove(s[l])
                l+=1
        
        return res