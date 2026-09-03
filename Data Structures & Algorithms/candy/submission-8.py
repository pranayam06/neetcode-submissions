class Solution:
    def candy(self, ratings: List[int]) -> int:

        # [3, 4, 5, 4, 3, 4] 
        # [3, 4, 5, 4, 3, 2] 1 + 2 + 3 + 2 + 1 + len(hill)

        n = len(ratings)
        
        
        res = n 
        inc = 0
        dec = 0
        candy = 0
        i = 1
        
        while(i < n): 
            if ratings[i] == ratings[i-1]: 
                i+=1 
                continue 
            inc = 0
            while (i < n and ratings[i] > ratings[i-1]): 
                inc += 1 
                res += inc 
                i+=1 
            dec = 0 
            while (i < n and ratings[i] < ratings[i-1]): 
                dec += 1
                res += dec 
                i+= 1
            res -= min(inc, dec)
        
        return res
            
                
            
                 
    
