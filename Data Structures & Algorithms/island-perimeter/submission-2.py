class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res += (i + 1 >= ROWS or grid[i + 1][j] == 0)
                    res += (j + 1 >= COLS or grid[i][j + 1] == 0)
                    res += (i - 1 < 0 or grid[i - 1][j] == 0)
                    res += (j - 1 < 0 or grid[i][j - 1] == 0)
        return res

            