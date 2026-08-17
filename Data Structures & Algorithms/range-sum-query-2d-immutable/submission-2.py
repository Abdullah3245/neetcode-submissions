class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [row[:] for row in matrix]
        self.ROWS = len(matrix)
        self.COLS =  len(matrix[0])
        self.rectangle_sum = [[0] * (self.COLS+ 1) for _ in range(self.ROWS + 1)]
        sum = 0
        for i in range(self.ROWS):
            prefix = 0
            for j in range(self.COLS):
                above = self.rectangle_sum[i][j + 1]
                prefix += self.matrix[i][j]
                self.rectangle_sum[i + 1][j + 1] = above + prefix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.rectangle_sum[row2][col2]
        above = self.rectangle_sum[row1 - 1][col2]
        left = self.rectangle_sum[row2][col1 - 1]
        topLeft = self.rectangle_sum[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)