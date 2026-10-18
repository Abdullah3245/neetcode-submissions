class UndergroundSystem:
    def __init__(self):
        self.cin = {}
        self.timing = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cin[id] = (t, stationName)    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        depature, start_station = self.cin[id]
        time = t - depature
        total_time, total_trips = self.timing.get((start_station, stationName), (0, 0))
        self.timing[(start_station, stationName)] = (total_time + time, total_trips + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trip = self.timing[(startStation, endStation)]
        return total_time / total_trip
