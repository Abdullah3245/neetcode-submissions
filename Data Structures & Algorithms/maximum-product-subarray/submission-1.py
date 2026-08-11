class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod = 1, 1
        res = max(nums)

        for num in nums:
            temp = max_prod * num
            # When we set the value to n we starting from a new position in the array 
            max_prod = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, temp, num * min_prod)
            res = max(res, max_prod)

        return res