class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        hmap = defaultdict(int) 
        res = 0

        while l <= r < len(s):
            while l < r and hmap[s[r]] > 0: 
                res = max(r-l, res)
                hmap[s[l]] -= 1
                l += 1
            hmap[s[r]] += 1
            r += 1
        res = max(r-l, res)

        return res
