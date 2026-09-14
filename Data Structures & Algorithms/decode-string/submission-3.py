class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        for index, c in enumerate(s):
            if c.isalnum() or c == '[':
                stack.append(c)

            elif c == ']':
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop() # remove the trailing '['
                count = ""

                while stack and stack[-1].isdigit():
                    count = stack.pop() + count

                
                stack.append(int(count) * string)
        
        return "".join(stack)