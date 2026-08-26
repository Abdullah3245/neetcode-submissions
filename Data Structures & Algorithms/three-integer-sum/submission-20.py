class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        res = []
        for index, k in enumerate(nums):
            i, j = index + 1, len(nums) - 1
            while i < j:
                key = tuple(sorted((nums[i], nums[j], k)))
                if nums[i] + nums[j] == -k and key not in triplets:
                    res.append(key)
                    triplets.add(key)
                elif nums[i] + nums[j] < -k:
                    i += 1
                else:
                    j -= 1
        return res
