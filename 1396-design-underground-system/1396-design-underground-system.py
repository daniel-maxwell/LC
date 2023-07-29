class UndergroundSystem:

    def __init__(self):
        self.userSystem = {}
        self.travelRecords = {}      

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.userSystem[id] = {"station": stationName, "time": t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        origin = self.userSystem[id]["station"]
        checkInTime = self.userSystem[id]["time"]

        if origin not in self.travelRecords:
            self.travelRecords[origin] = {stationName: [t - checkInTime]}

        elif stationName not in self.travelRecords[origin]:
            self.travelRecords[origin][stationName] = [t - checkInTime]
           
        else:
            self.travelRecords[origin][stationName].append(t - checkInTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        Sum = sum(self.travelRecords[startStation][endStation])
        return Sum / len(self.travelRecords[startStation][endStation])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)