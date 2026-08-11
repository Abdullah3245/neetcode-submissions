class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    visited = set()
                    # perform BFS for shortest distance
                    queue.append((i, j, 0))
                    while queue:
                        x, y, dist = queue.popleft()
                        grid[x][y] = min(dist, grid[x][y])
                        
                        if x + 1 < n and grid[x + 1][y] != -1 and (x + 1, y) not in visited:
                            queue.append((x + 1, y, dist + 1))
                            visited.add((x + 1, y))
                        if y + 1 < m and grid[x][y + 1] != -1 and (x, y + 1) not in visited:
                            queue.append((x, y + 1, dist + 1))
                            visited.add((x, y + 1))
                        if x - 1 >= 0 and grid[x - 1][y] != -1 and (x - 1, y) not in visited:
                            queue.append((x - 1, y, dist + 1))
                            visited.add((x - 1, y))
                        if y -1 >= 0 and grid[x][y - 1] != -1 and (x, y - 1) not in visited:
                            queue.append((x, y - 1, dist + 1))
                            visited.add((x, y - 1))