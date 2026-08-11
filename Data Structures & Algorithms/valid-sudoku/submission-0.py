class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW, COL = 9, 9

        def validSquare(start_row, start_col):
            num = set()
            for i in range(3):
                for j in range(3):
                    cell = board[start_row + i][start_col + j]
                    if cell == '.':
                        continue
                    if cell in num:
                        return False
                    num.add(cell)
            return True

        # Check rows
        for i in range(ROW):
            numbers = set()
            for j in range(COL):
                if board[i][j] == '.':
                    continue
                if board[i][j] in numbers:
                    return False
                numbers.add(board[i][j])

        # Check columns
        for j in range(COL):
            numbers = set()
            for i in range(ROW):
                if board[i][j] == '.':
                    continue
                if board[i][j] in numbers:
                    return False
                numbers.add(board[i][j])

        # Check 3x3 sub-boxes
        for i in range(3):
            for j in range(3):
                if not validSquare(i * 3, j * 3):
                    return False
        
        return True    