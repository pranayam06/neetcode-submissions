class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hmap = {
            "2": ["a", "b", "c"], 
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        def dfs(i, comb):
            if i == len(digits):
                res.append(comb)
            else:
                lets = hmap[digits[i]]
                for let in lets:
                    dfs(i+1, comb+let)
        if len (digits) == 0:
            return []
        dfs(0, "")
        return res




