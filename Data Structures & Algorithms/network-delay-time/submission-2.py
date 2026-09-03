class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        dist = [float('inf')] * (n + 1)
        graph = [[] for _ in range(n + 1)]

        for ui, vi, ti in times:
            graph[ui].append((vi, ti))

        dist[k] = 0
        dist[0] = 0
        heapq.heappush(heap, (dist[k], k))

        while heap:
            d, curr = heapq.heappop(heap)

            if d > dist[curr]:
                continue

            for neighbor, d in graph[curr]:
                if dist[curr] + d < dist[neighbor]:
                    dist[neighbor] = dist[curr] + d
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        
        max_time = max(dist)

        return max_time if max_time != float('inf') else -1