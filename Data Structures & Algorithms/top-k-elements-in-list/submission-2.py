class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqs = Counter(nums)
    
        mh = list([(-freq, num) for (num, freq) in freqs.items()])
        heapq.heapify(mh)


        for i in range(k):
            res.append(heapq.heappop(mh)[1])
        return res


