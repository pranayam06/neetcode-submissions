class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort by decreasing order of width and tie break by height  
        # picik an envelope, try to use it, memoize the max envelopes you have fit using this envelope 

        envelopes.sort(key=lambda x: (-x[0], -x[1]))
        dp = defaultdict(int)
        # just need to know whether we take the last envelope or not 
        for i, (w, h) in enumerate(envelopes): 
            # look at all previous envelope groupings 
            # we must TRY taking the envelope 
            for j in range(-1, i, 1):
                if j == -1: 
                    dp[i] = max(dp[i], 1)
                    continue
                w2 = envelopes[j][0]
                h2 = envelopes[j][1]
                if w2 > w and h2 > h: 
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp.values())


        



             

