class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        res.append([])
        N = len(nums)

        def backtrack(i):
            for i in range(i, N):
                sol.append(nums[i])
                res.append(sol[:])
                backtrack(i+1)
                if sol:
                    sol.pop()

        backtrack(0)
        return res