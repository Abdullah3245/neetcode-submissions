class MedianFinder:


    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.curr_elements = 0

    def addNum(self, num: int) -> None:
        if self.curr_elements == 0:
            heapq.heappush(self.min_heap, num)
            self.curr_elements = 1
            return 
        self.curr_elements += 1
        if self.min_heap[0] < num:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if len(self.min_heap) - len(self.max_heap) > 1:
            head = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -head)
        elif len(self.max_heap) - len(self.min_heap) > 1:
            head = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, head)

    def findMedian(self) -> float:
        median = None
        if self.curr_elements % 2 == 0:
            first = self.min_heap[0]
            second = -self.max_heap[0]
            
            median = float((first + second)) / 2.0
        else:
            if len(self.min_heap) > len(self.max_heap):
                median = float(self.min_heap[0])
            else:
                median = float(-self.max_heap[0])
        return median
        
        