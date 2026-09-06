class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        l = 0
        r = 0
        N = len(nums)
        jump = 0

        while r < N - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1 # prevents revisitation of the previous set
            r = farthest
            jump += 1

        return jump