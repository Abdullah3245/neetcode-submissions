class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = r = 0
        max_window = 1
        prev_diff = 0
        while r < len(arr) - 1:
            diff = arr[r + 1] - arr[r]

            if diff == 0:
                l = r + 1
            elif diff * prev_diff > 0: # a > b > c, just (b, c) for now
                l = r
            r += 1
            max_window = max(max_window, (r - l) + 1)
            prev_diff = diff

        
        return max_window
