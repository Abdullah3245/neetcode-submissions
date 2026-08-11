class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        output = 0
        
        for token in tokens:
            if token == '+':
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif token == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == '/':
                first = stack.pop()
                second = stack.pop()
                result = int(float(second) / float(first))
                stack.append(result)
            elif token == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            else:
                stack.append(int(token))
        
        return stack.pop()
        