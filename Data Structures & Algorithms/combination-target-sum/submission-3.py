class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        N = len(nums)
        def backtrack(i, sum):
            if sum == target:
                res.append(sol[:])
                return

            for i in range(i, N):
                if sum < target:
                    sol.append(nums[i])
                    sum += nums[i]
                    backtrack(i, sum)
                    curr = sol.pop()
                    sum -= curr 

        backtrack(0, 0)
        return res
