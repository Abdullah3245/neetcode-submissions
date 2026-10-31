class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]
        curr_min = 0
        min_min = nums[0]
        total = 0

        for i, num in enumerate(nums):
            total += num # for a circular subarray 

            # keeping tracking of the global maximum
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

            # keeping track of the global minimum
            curr_min = min(num, curr_min + num)
            min_min = min(curr_min, min_min)


        return max(max_sum, total - min_min) if max_sum > 0 else max_sum
        