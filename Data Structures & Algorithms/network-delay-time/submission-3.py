class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = defaultdict(list)
        for s, e, t in times: 
            adjlist[s].append((e, t))
        
        minheap = []

        heapq.heappush(minheap, (0, k))
        seen = set()
        res = 0

        while minheap: 
            
            t, node = heapq.heappop(minheap)
            if node in seen: 
                continue
            res = max(res, t)
            seen.add(node)
            if len(seen) == n: 
                return res
            for nbor, nbor_t in adjlist[node]: 
                heapq.heappush(minheap, (t + nbor_t, nbor))
        
        if len(seen) == n: 
            return res
        return -1
             
            
            
