class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = dict()
        for i,c in enumerate(order):
            order_index[c] = i

        # compare each word to the next 
       
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i + 1] 

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] == w2[j]:
                    continue
                if order_index[w1[j]] > order_index[w2[j]]:
                    return False
                break
        
        return True
                    
            

