import sys


class MinStack:
    def __init__(self):
        self.l = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if not self.min_list:
            self.min_list.append(val)
        else:
            min_val = min(val, self.min_list[-1])
            self.min_list.append(min_val)
    def pop(self) -> None:
        val = self.l[-1]
        self.l.pop()
        self.min_list.pop()
        return val

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
       return self.min_list[-1]
