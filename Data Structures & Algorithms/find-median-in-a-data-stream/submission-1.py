class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.n = 0 
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:
        if self.n == 0:
            heapq.heappush(self.maxheap, -1 *num)
        elif self.n == 1:
            if num < -1 * self.maxheap[0]:
                heapq.heappush(self.maxheap, -1 * num)
                heapq.heappush(self.minheap, -1 * heapq.heappop(self.maxheap))
            else:
                heapq.heappush(self.minheap, num)
        else:
            if num <= (-1 * self.maxheap[0]):
                heapq.heappush(self.maxheap, -1 * num)
            else:
                heapq.heappush(self.minheap, num)

            if len(self.maxheap) > (1 + len(self.minheap)):
                heapq.heappush(self.minheap, -1 * heapq.heappop(self.maxheap))
            elif len(self.minheap) > (1 + len(self.maxheap)):
                heapq.heappush(self.maxheap, -1 * heapq.heappop(self.minheap))
        self.n += 1

    def findMedian(self) -> float: 
        print(self.maxheap)
        print(self.minheap)
        if self.n % 2 == 1:
            if len(self.maxheap) > len(self.minheap):
                return -1 * self.maxheap[0]
            else:
                return self.minheap[0]
        else:
            return (-1 * self.maxheap[0] + self.minheap[0])/2
        
        