class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        elements = set()

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num not in elements:
                    curr.append(num)
                    elements.add(num)
                    backtrack()
                    curr.pop()
                    elements.remove(num)
    
        backtrack()
        return res