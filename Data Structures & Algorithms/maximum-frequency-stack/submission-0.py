class FreqStack:

    def __init__(self):
        self.queues = defaultdict(list)
        self.maxfreq = 0 
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        val_f = self.freq[val]
        self.maxfreq = max(val_f, self.maxfreq)
        self.queues[val_f].append(val) 
        

    def pop(self) -> int:
        res = self.queues[self.maxfreq].pop()
        if not self.queues[self.maxfreq]:
            self.maxfreq -= 1
        self.freq[res] -= 1
        return res



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()