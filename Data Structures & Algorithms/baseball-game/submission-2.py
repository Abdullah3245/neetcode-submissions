class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for op in operations:
            if op == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1 + num2)
            elif op == "C":
                stack.pop()
            elif op == "D":
                num1 = stack[-1]
                stack.append(num1 * 2)
            else:
                stack.append(int(op))
        
        return sum(stack)
