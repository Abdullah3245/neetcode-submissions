class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        while q:
            for _ in range(len(q)):
                x, y, t = q.popleft()
                t += 1
                if x + 1 < ROWS and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    time = max(t, time)
                    q.append((x + 1, y, t))
                if x - 1 >= 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    time = max(t, time)
                    q.append((x - 1, y, t))
                if y - 1 >= 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    time = max(t, time)
                    q.append((x, y - 1, t))
                if y + 1 < COLS and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    time = max(t, time)
                    q.append((x, y + 1, t))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return time