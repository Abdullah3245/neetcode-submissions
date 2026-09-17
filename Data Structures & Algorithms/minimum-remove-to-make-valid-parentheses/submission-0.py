class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        closing = 0
        opening = 0
        for c in s:
            if c == "(":
                stack.append(c)
                opening += 1
            elif c.isalpha():
                stack.append(c)
            if c == ")":
                if opening > closing:
                    stack.append(c)
                    closing += 1
        
        s = ""
        opening = 0
        i = 0
        while i < len(stack):
            if stack[i].isalpha():
                s += stack[i]
            elif stack[i] == ")":
                s += stack[i]
            elif stack[i] == "(" and closing > opening:
                opening += 1
                s += stack[i]
            i += 1
        return s
        
            