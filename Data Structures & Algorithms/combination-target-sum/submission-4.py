class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        N = len(nums)
        def backtrack(i, sum):
            if sum == target:
                res.append(sol[:])
                return

            if i >= N or sum > target:
                return 
            sol.append(nums[i])
            backtrack(i, nums[i] + sum)
            sol.pop()
            backtrack(i + 1, sum)

        backtrack(0, 0)
        return res
