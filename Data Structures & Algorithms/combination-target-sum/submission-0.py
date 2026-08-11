class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backTracking(result, current, index, nums, target):
            if sum(current) == target:
                result.append(current.copy())
                return

            if index >= len(nums) or sum(current) > target:
                return

            current.append(nums[index])
            backTracking(result, current, index, nums, target)
            current.pop()
            backTracking(result, current, index + 1, nums, target)

        backTracking(res, [], 0, nums, target)
        return res