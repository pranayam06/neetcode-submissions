class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], start: int, end: int, k: int) -> int:
        adjlist = defaultdict(list)
        for (src, dest, price) in flights:
            adjlist[src].append((dest, price))
        
        minheap = [] # (cost, node, k_left)
        hmap = {}

        heapq.heappush(minheap, (0, start, k))
        hmap[(start, k)] = 0

        while minheap: 
            cost, src, k_left = heapq.heappop(minheap)  
            if k_left == -1: 
                continue 

            if cost > hmap[(src, k_left)]:
                continue 

            for (dest, price) in adjlist[src]: 

                if (dest, k_left-1) not in hmap or (hmap[(dest, k_left-1)] > cost + price): 
                    hmap[(dest, k_left-1)] = cost + price 
                    heapq.heappush(minheap, (cost+price, dest, k_left-1))
            
        res = 100000
        for i in range(-1, k): 
            if (end, i) in hmap:
                res = min(hmap[(end, i)], res) 
        if res == 100000: return -1

        else: return res


