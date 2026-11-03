class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = second = third = False
        res = [-1, -1, - 1]
        for t in triplets:
            if t == target:
                return True
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                first = True
            if t[1] == target[1]:
                second = True
            if t[2] == target[2]:
                third = True
        return first and second and third