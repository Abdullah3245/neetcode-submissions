class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])

        def bfs(x, y):
            visited = set()
            curr_dist = 0
            q = deque()
            q.append((x, y, curr_dist))

            while q:
                x, y, distance = q.popleft()
                print(f"{distance} for {x} and {y}")
                grid[x][y] = min(distance, grid[x][y])
                if x + 1 < ROW and (x + 1, y) not in visited and grid[x + 1][y] > 0:
                    visited.add((x + 1, y))
                    print("appending")
                    q.append((x + 1, y, distance + 1))
                if x - 1 >= 0 and (x - 1, y) not in visited and grid[x - 1][y] > 0:
                    visited.add((x - 1, y))
                    print("appending")
                    q.append((x - 1, y, distance + 1))
                if y + 1 < COL and (x, y + 1) not in visited and grid[x][y + 1] > 0:
                    visited.add((x, y + 1))
                    print("appending")
                    q.append((x, y + 1, distance + 1))
                if y - 1 >= 0 and (x, y - 1) not in visited and grid[x][y - 1] > 0:
                    print("appending")
                    visited.add((x, y - 1))
                    q.append((x, y - 1, distance + 1))
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    bfs(i, j)       