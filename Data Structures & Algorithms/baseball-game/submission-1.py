class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        res = deque()
        for op in operations:
            if op == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                res.append(num1 + num2)
                stack.append(num1 + num2)
            elif op == "C":
                res.pop()
                stack.pop()
            elif op == "D":
                num1 = stack[-1]
                res.append(num1 * 2)
                stack.append(num1 * 2)
            else:
                stack.append(int(op))
                res.append(int(op))
        
        return sum(res)
