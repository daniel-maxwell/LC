class TimeMap:

    def __init__(self):
        self.storage = {}
        self.stamps = {}
        self.first = None
        self.prev = None
        self.prevKey = None
  
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.storage:
            self.storage[key][timestamp] = value
            self.stamps[key].append(timestamp)     
        else:
            self.storage[key] = {timestamp : value}
            self.stamps[key] = [timestamp]

        if not self.first: self.first = timestamp
        self.prev = timestamp
        self.prevKey = key


    def get(self, key: str, timestamp: int) -> str:

        if key not in self.storage:
            return ""

        if self.first and self.first > timestamp:
            return ""

        if key == self.prevKey and self.prev <= timestamp:
            return self.storage[key][self.prev]

        if timestamp in self.stamps[key]:
            return self.storage[key][timestamp]

        l, r = 0, len(self.stamps[key])
        m = l + ((r-l) // 2)

        while l <= r:
            if self.stamps[key][m] < timestamp:
                if m+1 == len(self.stamps[key]) or self.stamps[key][m+1] > timestamp:
                    return self.storage[key][self.stamps[key][m]]
                else:
                    l = m + 1
            else:
                r = m - 1
            m = l + ((r-l) // 2)
        return ""

                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)