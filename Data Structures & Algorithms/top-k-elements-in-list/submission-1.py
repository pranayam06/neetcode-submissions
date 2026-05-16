class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxheap = []
        for num, freq in freq.items():
            maxheap.append([-freq, num])
        heapq.heapify(maxheap)

        res = []

        for i in range(k):
            freq, num = heapq.heappop(maxheap)
            res.append(num)
        
        return res