class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening = set(["(", "[", "{"])
        close = set([")", "]", "}"])

        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            elif bracket in close:
                if not stack:
                    return False
                curr = stack.pop()
                if bracket == ")" and curr != "(":
                    return False
                if bracket == "]" and curr != "[":
                    return False
                if bracket == "}" and curr != "{":
                    return False
        if stack:
            return False
        return True