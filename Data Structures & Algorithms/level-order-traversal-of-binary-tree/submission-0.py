# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        l = []
        queue = [(root, 0)]

        while len(queue) > 0:
            curr, level = queue.pop(0)
            if len(l) > level:
                l[level].append(curr.val)
            else:
                l.append([curr.val])
            level += 1
            if curr.left:
                queue.append((curr.left, level))
            if curr.right:
                queue.append((curr.right, level))
            queue

        return l  