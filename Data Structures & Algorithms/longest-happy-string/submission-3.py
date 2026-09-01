class Heap: 
    def __init__(self): 
        self.heap = []
    
    def add(self, val): 
        heapq.heappush(self.heap, val)
    
    def pop(self): 
        return heapq.heappop(self.heap)
    
    

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        # example 
        # a = 3, b = 4, c = 2
        # pull from a heap getting the most. check if you have two consecutive same letters, then switch to another one 
        # a = 0, b = 1, c = 5
        # cc pop again 1 pop agiain 1
        # a = 0, b = 5, c = 10 
        # if you hit two sets of two , then try popping off three times 
        # then add them back onto the heap 

        heap = Heap()
        if a: heap.add((-a, "a"))
        if b: heap.add((-b, "b"))
        if c: heap.add((-c, "c"))
        res = ""
        temp = []

        while (heap.heap): 
            ct, ch = heap.pop()
            ct = -ct
            if len(res) >= 2: 
                if ch == res[-1] and ch == res[-2]:
                    temp = (-ct,ch) 
                    continue 
            res += ch
            

            if ct > 1: 
                heap.add((-(ct-1), ch))
            if temp: 
                heap.add(temp)
                temp = None
        
        return res
                
                    
            


        