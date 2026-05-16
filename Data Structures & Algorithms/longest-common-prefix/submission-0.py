class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            for j in range(0, len(prefix)):
                if (j >= len(strs[i]) or strs[i][j] != prefix[j]): 
                    print(prefix)
                    prefix = prefix[:j] 
                    break
        

        return prefix
                