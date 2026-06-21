class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} 
        

        for i in range(0,len(word1)+1): 
            for j in range(0, len(word2)+1): 
                if i == 0:
                    memo[(i,j)] = j
                elif j == 0: 
                    memo[(i,j)] =i
                else:
                    if word1[i-1] == word2[j-1]: 
                        nothing = memo[(i-1, j-1)]
                        memo[(i,j)] = nothing
                    else:
                        insert = 1 + memo[(i, j-1)]
                        delete = 1 + memo[(i-1, j)]
                        replace = 1 + memo[(i-1, j-1)]
                        memo[(i,j)] = min(insert, delete, replace)
        return memo[(len(word1), len(word2))]
                
            


            
