class StockSpanner:

    def __init__(self):
        self.prices = []
        self.numDays = 1
        self.yesterday = 10**5

    def next(self, price: int) -> int:

        if price >= self.yesterday:

            totalDays = self.numDays + 1
            i = len(self.prices) - self.numDays - 1

            while i >= 0 and price >= self.prices[i][0]:
                totalDays += self.prices[i][1]
                i -= self.prices[i][1]

            self.yesterday = price
            self.numDays = totalDays
            self.prices.append((price, self.numDays))
      
            return totalDays       

        else:
            self.yesterday = price
            self.numDays = 1
            self.prices.append((price, self.numDays))
            return 1


        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)