class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane algorithm
        res = max(nums)
        maxEnding = nums[0]
        minEnding = nums[0]

        for n in nums[1:]:
            if n == 0:
                maxEnding, minEnding = 1, 1
                continue
            temp = maxEnding * n
            maxEnding = max(maxEnding * n, n * minEnding, n)
            minEnding = min(temp, minEnding * n, n)
            
            res = max(res, maxEnding)
        
        return res