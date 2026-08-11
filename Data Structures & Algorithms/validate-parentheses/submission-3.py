class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for brackets in s:
            if brackets == '(' or brackets == '[' or brackets == '{':
                stack.append(brackets)
            elif len(stack) == 0:
                return False
            elif brackets == ')':
                curr = stack.pop()
                if curr != '(':
                    return False
            elif brackets == ']':
                curr = stack.pop()
                if curr != '[':
                    return False
            elif brackets == '}':
                curr = stack.pop()
                if curr != '{':
                    return False

        return len(stack) == 0