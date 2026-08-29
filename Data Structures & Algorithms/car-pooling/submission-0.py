class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minheap = []

        for (count, fro, to) in trips: 
            heapq.heappush(minheap, (fro, count))
            heapq.heappush(minheap, (to, -count))
        cur_passengers = 0 
        loc = 0
        while minheap: 
            loc = minheap[0][0]
            while minheap and minheap[0][0] == loc:
                (_, count) = heapq.heappop(minheap)
                cur_passengers += count 
        
            if cur_passengers > capacity: 
                return False  
        
        return True
            
                

            
