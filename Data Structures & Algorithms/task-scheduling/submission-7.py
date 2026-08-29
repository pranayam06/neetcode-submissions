class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # prioritize, next available, count
        #tie break 
        # lowest availability, highest count
        heap = []
        q = deque()
        # q keeps track of available 

        task_counts = defaultdict(int)
        for task in tasks: 
            task_counts[task] += 1
        
        for task, count in task_counts.items():
            heapq.heappush(heap, -count)     

        t = 1
        while (q or heap):
            if heap: 
                count = heapq.heappop(heap)
                count = -1 * count 
                if (count-1) > 0: 
                    q.append((t + n+1, count-1))
            if not heap and q: 
                t = q[0][0] 
            else: 
                t += 1
            while q and q[0][0] <= t: 
                heapq.heappush(heap, -q.popleft()[1]) 
        
        return t-1            


