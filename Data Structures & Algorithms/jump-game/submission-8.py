class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        N = len(nums) 
        curr = -1

        for i in range(N - 2, -1, -1):
            # Directly reach the goal
            if nums[i] + i >= N - 1:
                curr = i
            elif nums[i] + i >= curr and curr != -1:
                curr = i
        print(curr)
        return True if curr == 0 else False 
