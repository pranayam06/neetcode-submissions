class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int: 

        cap_heap = []
        prof_heap = []

        for i, cap in enumerate(capital): 
            heapq.heappush(cap_heap, (cap, i))
        ct = 0

        while (cap_heap or prof_heap) and ct < k:
            # add all affordable ones
            while (cap_heap and cap_heap[0][0] <= w):
                (cap, i) = heapq.heappop(cap_heap)
                heapq.heappush(prof_heap, -1*(profits[i])) 


            if not prof_heap: 
                return w 
            
            prof = -1 * heapq.heappop(prof_heap)
            ct += 1
            w += prof 
        
        return w
        

        