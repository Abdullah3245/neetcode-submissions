class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        area = 0
        while i < j:
            left = heights[i]
            right = heights[j]
            width = abs(i - j)
            height = min(left, right)
            area = max(area, height * width)
            if left > right:
                j -= 1
            else:
                i += 1
        return area