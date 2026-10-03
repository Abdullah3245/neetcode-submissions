class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        res.append([])
        N = len(nums)

        def backtrack(i):
            if i >= N:
                return

            # include nums[i]
            sol.append(nums[i])
            res.append(sol[:])
            backtrack(i+1)

            # not include nums[i]
            sol.pop()
            backtrack(i + 1)

        backtrack(0)
        return res