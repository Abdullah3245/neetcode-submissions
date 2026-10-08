class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        # store the maximum sum so far
        res = nums[0]

        # maximum sum of the current subarray
        maxEnding = nums[0]

        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i]) # include the current element or start a new subarray sum
            res = max(res, maxEnding)
        
        return res

