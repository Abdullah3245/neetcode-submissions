class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1 for i in range(n)]

        prefix_product[0] = 1
        prefix_product[1] = nums[0]

        for index in range(2, n):
            prefix_product[index] = prefix_product[index - 1] * nums[index - 1]

        print(prefix_product)

        suffix_product = [1 for i in range(n)]
        suffix_product[n - 1] = 1
        suffix_product[n - 2] = nums[n - 1]

        for index in range(n - 3, -1, -1):
            suffix_product[index] = nums[index + 1] * suffix_product[index + 1]
        
        print(suffix_product)

        product = [1 for i in range(n)]
        
        for i in range(n):
            product[i] = suffix_product[i] * prefix_product[i]
        
        return product