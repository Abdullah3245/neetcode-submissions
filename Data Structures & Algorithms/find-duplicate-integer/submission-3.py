class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = abs(num) - 1
            print(index)
            if nums[index] < 0:
                return abs(index) + 1
            else:
                nums[index] *= -1
        
        return -1