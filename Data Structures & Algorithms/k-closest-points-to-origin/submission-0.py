class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            dist = math.sqrt(dist)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, point))
            else:
                if max_heap[0][0] < -dist:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-dist, point))
        
        points_list = []
        for i in range(k):
            points_list.append((heapq.heappop(max_heap))[1])
        
        return points_list