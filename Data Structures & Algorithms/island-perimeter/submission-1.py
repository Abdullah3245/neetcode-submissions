class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        max_perimeter = 0
        ROWS, COLS = len(grid), len(grid[0])
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        # recursive dfs function
        def dfs(node):
            nonlocal max_perimeter
            x, y = node
            if (x, y) in visited:
                return
            visited.add((x, y))

            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if nx < 0 or nx >= ROWS or ny < 0 or ny >= COLS or grid[nx][ny] == 0:
                    max_perimeter += 1
                    continue
                dfs((nx, ny))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    dfs((i, j))
        
        return max_perimeter

            