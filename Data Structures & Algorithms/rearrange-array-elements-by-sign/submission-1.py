class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []

        positive, negative = 0, 0

        def next_pos():
            nonlocal positive
            while nums[positive] < 0 and positive < len(nums):
                positive += 1
        
        def next_neg():
            nonlocal negative
            while nums[negative] > 0 and negative < len(nums):
                negative += 1

        while positive < len(nums) and negative < len(nums):
            next_pos()
            next_neg()
            if positive >= len(nums) or negative >= len(nums):
                break
            res.append(nums[positive])
            res.append(nums[negative])
            positive += 1
            negative += 1
        
        return res