class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        # iterate through the list
        for a in asteroids:
            alive = True
            # check for different direction
            while stack and (a < 0 and stack[-1] > 0):
                if abs(a) > abs(stack[-1]): # compare size
            # if stack has smaller pop and add bigger to stack
                    stack.pop()
                # if both are same size, destroy both
                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                    alive = False
                    break
                else:
                    # stack has bigger so kill incoming
                    alive = False
                    break
            if alive:
                stack.append(a)
                                    
        # return the stack
        return list(stack)