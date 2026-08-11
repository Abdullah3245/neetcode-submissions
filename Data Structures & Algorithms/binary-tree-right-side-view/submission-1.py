# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_nodes = []

        q = deque()
        q.append(root)

        while len(q) > 0:
            length = len(q)
            rightSide = None
            
            for i in range(length):
                # pop from the front or start of the queue
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightSide:
                right_nodes.append(rightSide.val)
            
        return right_nodes
        