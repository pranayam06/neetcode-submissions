class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for _ in range(len(s) + 1)]
        memo[len(s)] = True


        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i+len(word)] == word:
                    if memo[i+len(word)] == True:
                        memo[i] = True 
        
        return memo[0]



