class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        h = []

        for value, freq in frequency.items():
            if len(h) < k:
                heapq.heappush(h, (freq, value))
            else:
                f, v = h[0]
                if freq > f:
                    heapq.heappushpop(h, (freq, value))
        top_k = [value for freq, value in h]
        return top_k

        