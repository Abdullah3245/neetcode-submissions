class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for p, s in pair:
            if not stack:
                reach_time = (target - p) / s
                stack.append(reach_time)
                continue
            curr_time = (target - p) / s
            if curr_time > stack[-1]:
                stack.append(curr_time)
        
        return len(stack)       