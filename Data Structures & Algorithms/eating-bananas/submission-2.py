class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)

        def helper(k):
            res = 0
            for pile in piles: 
                res += (pile + k - 1) // k # ceil 
            return res
        # brute force
        l, r = 1, n
        res = 0

        while (l <= r):
            m = l + ((r-l)//2)
            cur = helper(m)
            if (cur <= h):
                res = m 
                r = m - 1
            elif (cur > h):
                l = m+1
        return res
             
            

