class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:  # Changed from low <= high
            if nums[low] < nums[high]:  # Array is sorted, min is at low
                return nums[low]
                
            mid = (low + high) // 2  # Use // for integer division
            
            if nums[mid] > nums[high]:  # Changed condition
                # Minimum is in right half
                low = mid + 1
            else:
                # Minimum is in left half (including mid)
                high = mid  # Changed from mid - 1
        
        return nums[low]