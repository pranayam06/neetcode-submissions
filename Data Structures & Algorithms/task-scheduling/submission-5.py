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
            q.append((1, count))
        
        # current cycle 
        # available to do X @ 1 and Y @ 1
        # time = 2 
        # time + n = next available time 
        # time available of last = 1 
        # max(time, time available) = 2 
        # now we complete and time = 3 
        # next time available = 3+ n = 5 
         

        t = 1
        while (q or heap): 
            # push onto the queue all of the available ones 
            # then prioritize by count in the heap 
            while(q and q[0][0]<=t): 
                (time, count) = q.popleft()
                heapq.heappush(heap, (-count, time)) 
            # now heap only contains available ones
            if not heap: 
                t = q[0][0]
                continue
            (count, time) = heapq.heappop(heap) 
            new_ct = (-1*count) -1
            t = max(t, time) + 1
            if new_ct: 
                q.append((t+n, new_ct))
            
        
        return t-1
            


