class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        N = len(candidates)
        candidates.sort()

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            
            if curr_sum > target or i >= N:
                return 
            
            # include element at i
            sol.append(candidates[i])
            backtrack(i+1, curr_sum + candidates[i])
            sol.pop()

            # skp element at i
            while i + 1 < N and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr_sum)

        backtrack(0,0)
        return res
        