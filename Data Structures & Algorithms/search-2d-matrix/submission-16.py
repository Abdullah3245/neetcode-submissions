class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])


        top, bot = 0, ROWS - 1
        while top <= bot:
            mid = (bot + top) // 2

            if matrix[mid][0] <= target <= matrix[mid][COLS - 1]:
                break
            elif matrix[mid][0] < matrix[mid][COLS - 1] < target:
                top = mid + 1
            else:
                bot = mid - 1

        mid_row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False