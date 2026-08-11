class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findMinHelper(nums):
            # edge case no rotation or num.length rotation and array is still sorted
            if nums[0] < nums[-1]:
                return nums[0]
            low = 0
            high = len(nums) - 1
            mid = int((low + high) / 2)
            while low < high:
                if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
                    return nums[mid]
                if nums[low] > nums[mid]:
                    return findMinHelper(nums[mid - 1 : high + 1])
                else:
                    return findMinHelper(nums[mid + 1 : high + 1])
            return nums[mid]
        # Edge case array of size 1 => min remains the same regardless of rotations
        if len(nums) <= 1:
            return nums[0]
        return findMinHelper(nums)
        