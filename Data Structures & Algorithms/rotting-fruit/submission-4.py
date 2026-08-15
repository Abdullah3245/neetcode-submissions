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
            for _ in range(len(q)): # newly added nodes await
                x, y, t = q.popleft()
                t += 1
                directions = [(1,0), (-1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y 
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 1:
                        time = max(t, time)
                        grid[nx][ny] = 2
                        q.append((nx, ny, t))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return time