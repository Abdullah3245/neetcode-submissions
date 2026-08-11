class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, low, high) -> int:
            while low <= high:
                mid = (low + high) // 2
                # base case
                if nums[mid] == target:
                    return mid
                # left sorted portion
                if nums[low] <= nums[mid]:
                    if target > nums[mid] or target < nums[low]:
                        low = mid + 1
                    else:
                        high = mid - 1
                # right sorted portion
                else:
                    if target < nums[mid] or target > nums[high]:
                        high = mid - 1
                    else:
                        low = mid + 1

            return -1
        return binary_search(nums, target, 0, len(nums) - 1)    