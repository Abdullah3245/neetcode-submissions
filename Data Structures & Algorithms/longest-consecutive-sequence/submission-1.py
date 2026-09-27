class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        
        for num in nums:
            if num - 1 not in numSet: # we see a sub-sequence
                length = 1
                while (length + num) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest