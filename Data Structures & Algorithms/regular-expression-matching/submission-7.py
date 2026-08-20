class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def help(s_i, p_i): 
            if p[p_i] == ".": 
                return True 
            else: 
                return s[s_i] == p[p_i]

        
        def match(s_i, p_i): 
            if p_i >= len(p): 
                return (s_i == len(s))
            if s_i >= len(s): 
                if p_i >= len(p):
                    return True
                if p_i + 1 < len(p) and p[p_i + 1] == "*":
                    return match(s_i, p_i + 2)
                return False
            if (s_i, p_i) in dp: 
                return dp[(s_i, p_i)]
            
            if p_i < len(p) - 1:
                if p[p_i+1] == "*": 
                    dp[(s_i, p_i)] = match(s_i, p_i+2) or (help(s_i,p_i) and match(s_i+1, p_i))
                    return dp[(s_i, p_i)]
            if p[p_i] == ".": 
                dp[(s_i, p_i)] = match(s_i+1,p_i+1)
                return dp[(s_i, p_i)]
            dp[(s_i, p_i)] = p[p_i] == s[s_i] and match(s_i+1, p_i+1)
            return dp[(s_i, p_i)]
        
        match(0, 0)
        return dp[(0,0)]
            
