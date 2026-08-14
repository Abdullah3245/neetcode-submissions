# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()

        q.append((root, 0))

        l = []

        while q:
            curr, level = q.popleft()


            if len(l) < level + 1:
                l.append([curr.val])
            else:
                l[level].append(curr.val)
            
            left, right = curr.left, curr.right

            if left:
                q.append((left, level + 1))
            if right:
                q.append((right, level + 1))
        
        return l