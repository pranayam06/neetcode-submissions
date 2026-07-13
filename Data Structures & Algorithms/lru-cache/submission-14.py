class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {} # val, recently used
        self.t = 0
        self.capacity = capacity 
        self.size = 0 
        # higher t = more recent

    def get(self, key: int) -> int:         
        print(self.hmap)

        self.t += 1
        if key in self.hmap:
            self.hmap[key][1] = self.t
            return self.hmap[key][0]
        return -1

        

    def put(self, key: int, value: int) -> None: 
        print(self.hmap)
        self.t += 1
        if key in self.hmap:
            self.hmap[key] = [value, self.t]
            return
        if self.size == self.capacity:
            min_t = 1000000
            min_key = 0
            for k, [v, t] in self.hmap.items():
                if t < min_t:
                    min_key = k 
                    min_t = t
            del self.hmap[min_key]
            self.size -= 1

        self.hmap[key] = [value, self.t]
        self.size += 1



        
