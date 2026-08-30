class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.arr.append(val)
        self.hmap[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        idx = self.hmap[val]
        if idx == len(self.arr)-1: 
            self.arr.pop()
            del self.hmap[val]
        else:
            rep = self.arr[-1]
            rep_i = self.hmap[rep]
            self.arr[idx] = self.arr[rep_i]
            self.hmap[rep] = idx
            self.arr.pop()
            del self.hmap[val]
        return True 


    def getRandom(self) -> int:
        r = random.randint(0, len(self.arr)-1)
        return self.arr[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()