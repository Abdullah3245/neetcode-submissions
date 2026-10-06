class MyCircularQueue:

    def __init__(self, k: int):
        self.l = [0] * k
        self.start, self.end = -1, -1
        self.k = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        # Queue is full
        if self.count == self.k:
            return False

        if self.isEmpty():
            self.start = 0
            self.end = 0
        else:
        # inserting for first time or wrapping around
            self.end = (self.end + 1) % self.k

        self.l[self.end] = value
        self.count += 1
        return True 

    def deQueue(self) -> bool:
        # Empty Queue 
        if self.isEmpty():
            return False

        self.count -= 1

        # queue is empty now
        if self.count == 0:
            self.start = -1
            self.end = -1
            return True
        
        self.start = (self.start + 1) % self.k
    
        return True
        

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.l[self.start]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.l[self.end]

    def isEmpty(self) -> bool:
        return self.start == -1

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()