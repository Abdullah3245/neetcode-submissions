class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        max_window = 1
        prev_sign = ""
        
        while r < len(arr):
            if arr[r - 1] > arr[r] and prev_sign != ">":
                max_window = max(max_window, (r - l) + 1)
                r += 1
                prev_sign = ">"
            elif  arr[r - 1] < arr[r] and prev_sign != "<":
                max_window = max(max_window, (r - l) + 1)
                r += 1
                prev_sign = "<"
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                prev_sign = ""
        return max_window
