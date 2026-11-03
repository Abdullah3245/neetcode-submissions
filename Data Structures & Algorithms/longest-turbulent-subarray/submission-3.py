class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 0
        max_window = 1
        prev_sign = ""
        
        while r < len(arr) - 1:
            if arr[r] > arr[r + 1] and prev_sign != ">":
                r += 1
                max_window = max(max_window, (r - l) + 1)
                prev_sign = ">"
            elif  arr[r] < arr[r + 1] and prev_sign != "<":
                r += 1
                max_window = max(max_window, (r - l) + 1)
                prev_sign = "<"
            else:
                r = r + 1 if arr[r + 1] == arr[r] else r
                l = r
                prev_sign = ""
        return max_window
