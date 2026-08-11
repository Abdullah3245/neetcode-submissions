class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Marking the rows and columns which need to be set to zero
        zero = False
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        zero = True

        for row in range(1, len(matrix)):
           for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        if zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        