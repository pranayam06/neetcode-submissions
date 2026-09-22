class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0 
        r = 0 

        goal = dict()
        for ch in t: 
            if ch not in goal: 
                goal[ch] = 1
            else:
                goal[ch] += 1
        
        def ok(freq):
            for k, v in freq.items():
                if v > 0: 
                    return False
            return True

        res_len = len(s) + 1 
        res = ""

        while l <= r < len(s): 
            # we always havent taken r at this point 
            # if its in goal, then we care 
            if s[r] in goal: 
                goal[s[r]] -= 1
            r += 1
            while ok(goal): 
                if r-l <= res_len: 
                    
                    res = s[l:r]
                    res_len = r-l
                # pop l and try check 
                if l < r:
                    if s[l] in goal: 
                        goal[s[l]]+= 1
                    l += 1
                else: 
                    break 
        
        return res
        
            
                



