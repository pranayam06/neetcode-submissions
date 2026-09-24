class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        freqs = Counter(nums)
        heap = []
        for k, v in freqs.items(): 
            heapq.heappush(heap, (v, k))

            while (heap and len(heap) > K): 
                heapq.heappop(heap)
    
        res = []
        for k, v in heap:
            res.append(v)
        return res[::-1]