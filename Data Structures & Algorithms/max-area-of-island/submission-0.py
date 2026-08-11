class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        l = [0]

        ROW = len(grid)
        COL = len(grid[0])

        def dfs(r, c, visited):
            if r >= ROW or c >= COL or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            l[0] += 1
            dfs(r + 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r - 1, c, visited)
            dfs(r, c - 1, visited)

        max_area = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] != 0 and (i, j) not in visited:
                    dfs(i, j, visited)
                    print(l[0])
                    max_area = max(max_area, l[0])
                l[0] = 0

        return max_area      