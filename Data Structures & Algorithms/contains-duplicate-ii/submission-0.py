class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l, r = 0, 0

        for index, num in enumerate(nums):
            if (index - l) > k:
                print(index)
                window.remove(nums[l])
                l += 1
            if num in window:
                return True
            window.add(num)
        return False