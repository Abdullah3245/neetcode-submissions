class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store.keys():
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys():
            return ""
        l = self.store[key]
        low, high = 0, len(l) - 1
        seen = 0
        res = ""
        while low <= high:
            mid = (low + high) // 2
            val, stamp = l[mid]
            if stamp <= timestamp:
                res = val
                low = mid + 1
            else:
                high = mid - 1
        return res
