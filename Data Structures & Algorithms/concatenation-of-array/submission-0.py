class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cat = nums[:]

        for num in nums:
            cat.append(num)
        return cat