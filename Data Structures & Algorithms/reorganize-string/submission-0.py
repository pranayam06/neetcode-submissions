class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        count = Counter(s) 
        maxheap= []
        for char, freq in count.items():
            maxheap.append((-freq, char))
        heapq.heapify(maxheap)
        # if idle, then return empty string  
        prev = None

        while maxheap or prev: 
            if maxheap:
                cur = heapq.heappop(maxheap)
                if prev: 
                    heapq.heappush(maxheap, prev) 
                res.append(cur[1])
                ct = cur[0] + 1
                if ct != 0:
                    prev = (ct, cur[1]) 
                else:
                    prev = None
            else:
                return "" 
        
        return "".join(res)

                


            

                 
