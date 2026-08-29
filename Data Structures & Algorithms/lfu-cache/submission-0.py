class LFUCache:

    def __init__(self, capacity: int):
        self.t = 0
        self.cap = capacity 
        self.last_access = dict()
        self.freq = defaultdict(int)
        self.hmap = dict()
        self.minheap = []

    def get(self, key: int) -> int: 
        # increases frequency and recency by key
        if key in self.hmap: 
            self.last_access[key] = self.t 
            self.freq[key] += 1
            self.t+=1 
            heapq.heappush(self.minheap, (self.freq[key], self.last_access[key], key))
            return self.hmap[key]
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if not(len(self.hmap) < self.cap or key in self.hmap):
            self.evict() 
        self.hmap[key] = value 
        self.last_access[key] = self.t 
        self.freq[key] += 1
        heapq.heappush(self.minheap, (self.freq[key], self.last_access[key], key))
        self.t += 1
    
    def evict(self): 
        while self.minheap: 
            (freq, t, key) = heapq.heappop(self.minheap)
            if self.last_access[key] == t:
                break 
        
        if key in self.hmap: del self.hmap[key]
        if key in self.last_access: del self.last_access[key]
        if key in self.freq: del self.freq[key] 

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)