class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        i = 0
        N = len(nums)
        jump = 0

        while i < N - 1:
            max_jump = nums[i] + i
            for j in range(i + 1, i + nums[i] + 1):
                if j >= N - 1:
                    max_jump = N - 1
                    i = N - 1
                    break
                if max_jump < nums[j] + j:
                    max_jump = nums[j] + j
                    i = j
            jump += 1

        return jump