# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = [True]
        def dfs(root) -> int:

            if root is None:
                return 0     

            left_height = dfs(root.left)
            right_height = dfs(root.right) 

            if abs(left_height - right_height) > 1:
                is_balanced[0] = False

            return 1 + max(left_height, right_height)
        # Edge case
        if root is None:
            return True
        dfs(root)

        return is_balanced[0]