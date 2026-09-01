class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def speed(k):
            curr = 0
            for p in piles:
                curr += math.ceil(p / k)
            return curr

        l, r = 1, max(piles)
        min_speed = float('inf')
        while l <= r:
            m = (l + r) // 2
            curr = speed(m)
            if curr > h:
                l = m + 1
            else:
                r = m - 1
                min_speed = min(min_speed, m)
        return min_speed
