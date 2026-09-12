class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        # o(d) where d = len(dictionary)
        res = []
        arr = []

        def bt(l, r):
            
            if l == len(s): 
                res.append(' '.join(arr))
                return 
            if r > len(s): 
                return

            # exclude r 
            if s[l:r] in words: 
                arr.append(s[l:r])
                bt(r, r)
                arr.pop()
            bt(l, r+1)
            return
        
        bt(0,0)
        return res