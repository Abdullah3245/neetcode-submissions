class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        for x, y in trust:
            in_degree[y] += 1
            out_degree[x] += 1
        
        for index, d in enumerate(in_degree[1:]):
            if d == n - 1 and out_degree[index + 1] == 0:
                return index + 1
        return -1

