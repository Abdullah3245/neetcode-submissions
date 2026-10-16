class MyStack:

    def __init__(self):
        self.deque1 = deque()
        self.deque2 = deque()

    def push(self, x: int) -> None:
        self.deque1.append(x)        

    def pop(self) -> int:
        while len(self.deque1) > 1:
            self.deque2.append(self.deque1.popleft())
        self.deque1, self.deque2 = self.deque2, self.deque1
        return self.deque2.popleft()

    def top(self) -> int:
        return self.deque1[-1]

    def empty(self) -> bool:
        return max(len(self.deque1), len(self.deque2)) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()