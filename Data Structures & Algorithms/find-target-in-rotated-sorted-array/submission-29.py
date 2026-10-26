class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        pivot = l
        def binary_search(l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid 
                if nums[mid] < target: # we are smaller so move towards greater values
                    l = mid + 1
                elif nums[mid] > target: # we are greater so move towards smaller values
                    r = mid - 1
            
            return -1
        
        res = binary_search(0, pivot - 1, target)

        if res != -1:
            return res
        
        return binary_search(pivot, len(nums) - 1, target)
            