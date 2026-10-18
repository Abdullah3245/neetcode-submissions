class UndergroundSystem:
    def __init__(self):
        self.cin = {}
        self.station = {}
        self.timing = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cin[id] = t
        self.station[id] = stationName
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        depature = self.cin[id]
        time = t - depature
        total_time, total_trips = self.timing.get((self.station[id], stationName), (0, 0))
        self.timing[(self.station[id], stationName)] = (total_time + time, total_trips + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trip = self.timing[(startStation, endStation)]
        return total_time / total_trip
