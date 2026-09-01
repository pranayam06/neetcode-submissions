class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg = 1
        pos = 0
        res = -float('inf')
        
        for num in nums: 
            pos = max(1,pos)
            if num < 0: 
                pos, neg = neg * num, pos * num 
            if num > 0: 
                pos = pos * num 
                neg = neg * num 
            if num == 0: 
                neg = pos = 0  

            res = max(pos, max(res, neg))

            
        return res

            
            
                