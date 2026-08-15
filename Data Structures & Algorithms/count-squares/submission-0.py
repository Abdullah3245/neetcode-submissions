class CountSquares:

    def __init__(self):
        self.points_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points_count[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or (x == px or y == py):
                continue
            res += self.points_count[(x, py)] * self.points_count[(px, y)]
        return res

