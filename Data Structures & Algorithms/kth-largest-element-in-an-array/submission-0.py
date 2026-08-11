class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for index, num in enumerate(nums):
            if len(heap) < k:
                heapq.heappush(heap, (num, index))
            else:
                top, index = heap[0]
                if num > top:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (num, index))
        
        top, index = heap[0]
        return top