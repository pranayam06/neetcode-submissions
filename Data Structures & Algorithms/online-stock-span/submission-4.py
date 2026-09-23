class StockSpanner:
    # we almost dont care if the price goes lower or equal 

    def __init__(self): 
        self.stocks = [] 
        self.ct = 0 

        

    def next(self, price: int) -> int: 
        # nothing greater than it has been seen 
        res = 0
        while (self.stocks and self.stocks[-1][0] <= price):
            self.stocks.pop()
        if not self.stocks: 
            res=  self.ct  
        else: 
            res = self.ct -self.stocks[-1][1]
        
        self.ct += 1
        self.stocks.append((price, self.ct))
        return res +1 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)