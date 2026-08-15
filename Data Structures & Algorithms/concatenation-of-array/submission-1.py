class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cat = nums[:] # shallow copy, not an alias

        for num in nums:
            cat.append(num)
        return cat