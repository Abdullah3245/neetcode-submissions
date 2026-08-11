class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        profit = [0] * (n - 1)
        profit[0] = nums[0]
        profit[1] = max(nums[0], nums[1])

        for i in range(2, n - 1):
            profit[i] = max(profit[i - 1], profit[i - 2] + nums[i])

        profit2 = [0] * (n)
        profit2[1] = nums[1]

        if n > 2:
            profit2[2] = max(nums[1], nums[2])

        for i in range(3, n):
            profit2[i] = max(profit2[i - 1], profit2[i - 2] + nums[i])

        return max(profit2[n - 1], profit[n - 2])