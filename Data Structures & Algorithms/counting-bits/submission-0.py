class Solution:
    def countBits(self, n: int) -> List[int]: 
        output = []
        for num in range (0, n+1):
            count = 0 
            for i in range (32):
                count += 1 & (num >> i)
            output.append(count)
        
        return output


        