class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(x, y):
            if (x, y) in visited:
                return
            if x >= ROWS:
                return 
            if x < 0:
                return 
            if y >= COLS:
                return 
            if y < 0:
                return
            if grid[x][y] == "0":
                return 
            visited.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        num_island = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    num_island += 1
        return num_island