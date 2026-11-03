class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        N = len(s)
        r = N - 1
        for i in range(N):
            if s[i] == "(":
                left_min += 1
                left_max += 1
            if s[i] == "*":
                left_max += 1
                left_min = max(0, left_min - 1)
            if s[i] == ')':
                left_max -= 1
                left_min = max(0, left_min - 1)
            if left_max < 0:
                return False
        
        return left_min == 0