class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        n = len(temperatures)

        for index, temp in enumerate(temperatures):
            if stack and temp <= stack[-1][0]:
                stack.append((temp, index))
            elif not stack:
                stack.append((temp, index))
            elif stack and stack[-1][0] < temp:
                print(f"{temp} is greater than {stack[-1][0]}")
                result[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
                stack.append((temp, index))
                for i in range(len(stack) - 2, - 1, -1):
                    if stack[i][0] < stack[-1][0]:
                        result[stack[i][1]] = stack[-1][1] - stack[i][1]
                        stack.pop(i)
                    else:
                        break

        return result     