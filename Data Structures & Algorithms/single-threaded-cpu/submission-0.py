class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # minheap 
        # sorted array 
        tasks = deque(sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)]))

        res = []
        minheap = []

        time = 0

        while minheap or tasks:
            while tasks and tasks[0][0] <= time:
                heapq.heappush(minheap, tuple(tasks.popleft()[1:]))
            if minheap: 
                processing = heapq.heappop(minheap)
                res.append(processing[1])
                time += processing[0]
            else: 
                time = tasks[0][0]
        
        return res
            


