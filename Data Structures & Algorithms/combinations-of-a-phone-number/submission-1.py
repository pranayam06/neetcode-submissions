class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def bt(i, letters): 
            if i == len(digits):
                if len(letters): 
                    res.append(''.join(letters))
                return
            for char in digitToChar[digits[i]]:
                letters.append(char)
                bt(i+1, letters)
                letters.pop()
        
        bt(0, [])
        return res
            