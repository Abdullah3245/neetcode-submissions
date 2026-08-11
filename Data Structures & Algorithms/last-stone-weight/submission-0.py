class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for s in stones:
            heapq.heappush(max_heap, -s)
        
        while len(max_heap) > 1:
            max1 = - (heapq.heappop(max_heap))
            max2 = - (heapq.heappop(max_heap))
            new_weight = max1 - max2
            heapq.heappush(max_heap, -new_weight)
        
        return -max_heap[0]        