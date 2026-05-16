class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap) # max heap basically

        while (len(minHeap) > 1):
            a = heapq.heappop(minHeap) # abs(greater/=)
            b = heapq.heappop(minHeap)

            heapq.heappush(minHeap, (b-a)*(-1))
        
        if minHeap:
            return abs(minHeap[0])
        else:
            return 0




