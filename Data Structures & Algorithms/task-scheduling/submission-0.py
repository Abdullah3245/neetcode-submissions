class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = {}

        # Starting by counting the frequencies
        for task in tasks:
            if task in frequency.keys():
                frequency[task] += 1
            else:
                frequency[task] = 1

        max_heap = []

        for key, value in frequency.items():
            print(value)
            heapq.heappush(max_heap, (-value))

        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                f = 1 + heapq.heappop(max_heap)
                if f != 0:
                    queue.append([f, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, (queue.popleft()[0]))
        
        return time