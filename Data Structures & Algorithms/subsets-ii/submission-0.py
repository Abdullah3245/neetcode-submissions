class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res, subset = [], []

        def backtrack(i):
            if i >= N:
                return 
            
            # include nums[i]
            subset.append(nums[i])
            res.append(subset[:])
            backtrack(i + 1)
            # remove duplicates
            while i < N - 1 and nums[i] == nums[i + 1]:
                i += 1
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        res.append([])
        return res

