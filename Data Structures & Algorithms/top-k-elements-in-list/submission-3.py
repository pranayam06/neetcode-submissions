class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = defaultdict(int)
        for num in nums: 
            freqCounter[num] += 1 
        
        freqMap = defaultdict(list)
        for num, freq in freqCounter.items():
            freqMap[freq].append(num)
        
        res = []
        for f in range(len(nums), 0, -1): 
            res += freqMap[f]
            if len(res) == k: 
                return res