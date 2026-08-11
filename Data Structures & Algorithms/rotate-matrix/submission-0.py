class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # To rotate a matrix by 90 degrees we can compute the transpose and swap columns in any order
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                print(matrix)

        # Now we will swap the columns
        for i in range(len(matrix)):
            for j in range(int (len(matrix) / 2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix) - (j + 1)]
                matrix[i][len(matrix) - (j + 1)] = temp
        