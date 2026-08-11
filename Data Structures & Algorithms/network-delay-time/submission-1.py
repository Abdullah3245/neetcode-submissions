class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # We will implement djikstra algorithm
        graph = [[] for _ in range(n + 1)]

        for curr in times:
            graph[curr[0]].append((curr[1], curr[2]))

        distance = [sys.maxsize] * (n + 1)

        distance[k] = 0
        min_heap = [(distance[i], i) for i in range(len(distance))]
        heapq.heapify(min_heap)
        print(min_heap)

        q = deque()
        q.append(k)

        while q:
            curr = q.popleft()
            for neighbor, weight in graph[curr]:
                if distance[curr] + weight < distance[neighbor]:
                    distance[neighbor] = distance[curr] + weight
                    heapq.heappush(min_heap, (distance[neighbor], neighbor))
                    q.append(neighbor)
        
        print(distance)
        for dist in distance[1:]:
            if dist == sys.maxsize:
                return -1
        
        return max(distance[1:])