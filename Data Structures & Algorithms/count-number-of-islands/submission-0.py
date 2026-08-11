class Solution:
        def numIslands(self, grid: List[List[str]]) -> int:
            # We will perform DFS to count the number of connected components
            def dfs(grid, r, c, visited):
                if  r >= len(grid) or r < 0 or c >= len(grid[r]) or c < 0 or grid[r][c] == "0" or (r, c) in visited:
                    return
                visited.add((r, c))
                dfs(grid, r + 1, c, visited)
                dfs(grid, r, c + 1, visited)
                dfs(grid, r - 1, c, visited)
                dfs(grid, r, c - 1, visited)
            visited = set()
            num_island = 0
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == "1" and (r, c) not in visited:
                        dfs(grid, r, c, visited)
                        num_island += 1
            
            return num_island
            