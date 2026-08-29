class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minheap = []
        d = defaultdict(int)

        for (count, fro, to) in trips: 
            d[fro] += count
            d[to] -= count
        cur_passengers = 0 
        loc = 0

        for i in range(1001): 
            cur_passengers += d[i]
            if cur_passengers > capacity: 
                return False
        
        return True
            
                

            
