class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        maxheap = [-(ct) for ct in count.values()]
        heapq.heapify(maxheap)
        cur = 0
    
        while maxheap or q:
            cur += 1

            if not maxheap:
                cur = q[0][1]
            else: 
                cnt = heapq.heappop(maxheap) + 1
                if cnt != 0:
                    q.append([cnt, cur + n])  

            if q and q[0][1] == cur: 
                heapq.heappush(maxheap, q.popleft()[0])
        return cur


