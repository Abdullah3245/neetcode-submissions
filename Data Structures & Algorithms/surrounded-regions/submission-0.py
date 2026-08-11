class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        visited = set()

        def dfs(x, y):
            if x < 0 or x >= ROW or y < 0 or y >= COL or (x, y) in visited or board[x][y] != 'O':
                return
            visited.add((x, y))
            board[x][y] = '#'
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        # Marking unsurrounded region
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O' and (i in [0, ROW - 1] or j in [0, COL - 1]):
                    dfs(i, j)
        
        # marking sorrounded region
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == '#':
                    board[i][j] = 'O'       