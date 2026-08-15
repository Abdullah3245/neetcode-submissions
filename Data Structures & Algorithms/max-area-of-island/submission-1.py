class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        def dfs(x, y):
            if (x < 0 or x >= ROWS or 
            y < 0 or y >= COLS or (x,y) in visited or
            grid[x][y] == 0):
                return 0
            visited.add((x, y))
            area = 1
            area += dfs(x + 1, y)
            area += dfs(x - 1, y)
            area += dfs(x, y + 1)
            area += dfs(x, y - 1)
            return area
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(dfs(i, j), max_area)
        
        return max_area