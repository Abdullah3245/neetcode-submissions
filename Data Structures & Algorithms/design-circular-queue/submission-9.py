class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.l = -1
        self.r = -1
        self.count = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.k:
            return False
        
        if self.count == 0:
            self.l = 0
            self.r = 0
        else:
            self.r = (self.r + 1) % self.k
        self.q[self.r] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        if self.count == 1:
            self.l = -1
            self.r = -1
        else:
            self.l = (self.l + 1) % self.k
        self.count -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.l]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.r]

    def isEmpty(self) -> bool:
        return self.count == 0

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