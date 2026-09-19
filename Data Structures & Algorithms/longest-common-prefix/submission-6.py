class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = len(strs[0])
        # min between common prefix of pairwise
        for i in range(len(strs)-1):
            cur = 0 
            s1 = strs[i]
            s2 = strs[i+1]
            while cur < len(s1) and cur < len(s2) and s1[cur] == s2[cur]: 
                cur += 1  
            res = min(res, cur) 
            if not res: 
                return ""

        return strs[0][0:res]


            