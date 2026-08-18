class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # prefix product
        prefix_product = [1] * N # product of first should be 1
        # suffix product
        suffix_product = [1] * N # product of last should be 1
        
        for i in range(1, N):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        for i in range(N - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
        
        product = [suffix * prefix for suffix, prefix in zip(suffix_product, prefix_product)]
        
        return product