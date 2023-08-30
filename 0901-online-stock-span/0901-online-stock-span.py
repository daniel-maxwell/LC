class StockSpanner:

    def __init__(self):
        self.dayStack = []
        self.span = 0
        self.maxPrice = 0
        

    def next(self, price: int) -> int:
        self.span = 0
        self.dayStack.append(price)
        if price >= self.maxPrice:
            self.maxPrice = price
            return len(self.dayStack)

        i = len(self.dayStack) - 1

        while i >= 0 and self.dayStack[i] <= price:
            self.span += 1
            i -= 1
        
        return self.span


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)