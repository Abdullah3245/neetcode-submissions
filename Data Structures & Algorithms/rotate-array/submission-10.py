class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotation = k % len(nums) - 1
        
        def reversal(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reversal(0, len(nums) - 1)
        reversal(0, rotation)
        reversal(rotation + 1, len(nums) - 1)

