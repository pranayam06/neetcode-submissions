class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # map each char to its index to determine dependencies then just traverse adjacent words to make sure they match
        dc = {}
        for i, ch in enumerate(order):

            dc[ch] = i 

        for i in range(len(words)-1): 
            # compare adjacent words 
            l=0 
            while l < min(len(words[i]), len(words[i+1])) and words[i][l] == words[i+1][l]: 
                # good continue
                l+=1 

            if l == len(words[i+1]): 
                return False 
            elif l == len(words[i]): 
                continue
            if dc[words[i][l]] >  dc[words[i+1][l]]: 
                return False 
        return True