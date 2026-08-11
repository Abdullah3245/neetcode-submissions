class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_row = 0
        max_row = len(matrix)
        min_col = 0
        max_col = len(matrix[0])
        l = []

        while min_col < max_col and min_row < max_row:
            for i in range(min_col, max_col):
                l.append(matrix[min_row][i])
            min_row += 1

            for i in range(min_row, max_row):
                l.append(matrix[i][max_col - 1])
            max_col -= 1

            if not(min_row < max_row and min_col < max_col):
                break

            for i in range(max_col - 1, min_col - 1, -1):
                l.append(matrix[max_row - 1][i])
            max_row -= 1

            for i in range(max_row - 1, min_row - 1, -1):
                l.append(matrix[i][min_col])
            min_col += 1
        
        
        return l
