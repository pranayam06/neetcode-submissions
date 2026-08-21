class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0 for _ in range(len(w))]
        self.w = w
        for i in range(len(w)): 
            self.prefix[i] = self.w[i] + self.prefix[i-1]

    def pickIndex(self) -> int:
        val = random.randint(1, self.prefix[-1])
        l = 0
        r = len(self.prefix)
        while (l < r):
            m = l + (r-l)//2
            if self.prefix[m]>=val:
                r = m
            else:
                l = m +1
        return l 



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()