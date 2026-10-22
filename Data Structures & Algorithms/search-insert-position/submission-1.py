class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # edge cases
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        # binary search
        def binary_search():
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    return mid
                if target > nums[mid - 1] and target < nums[mid]:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        return binary_search()
