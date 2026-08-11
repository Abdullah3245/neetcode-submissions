class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_index = -1
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(float(p) / mid)
            print(total)
            if total > h:
                l = mid + 1
            else:
                min_index = mid
                r = mid - 1

        return min_index
        