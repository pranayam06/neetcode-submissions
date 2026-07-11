class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjlist = defaultdict(list)
        for (u, v, t) in times: 
            adjlist[u].append((v, t))
        
        minheap = []
        heapq.heappush(minheap, (0, k))
        hmap = {}
        hmap[k] = 0
        ctr = 1

        while minheap: 
            print (ctr)
            (mintime, node) = heapq.heappop(minheap)
            if mintime > hmap[node]:
                continue
            for (dest, time) in adjlist[node]: 
                if (dest in hmap and hmap[dest] > (mintime+time)) or dest not in hmap: 
                    hmap[dest] = mintime + time
                    heapq.heappush(minheap, (mintime+time, dest))
                    ctr += 1
        
        if len(hmap.keys()) == n: 
            return max(hmap.values())
        else: 
            return -1
            
        


