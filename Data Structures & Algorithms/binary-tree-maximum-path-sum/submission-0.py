# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = [root.val]

        # computing without a split
        def post_order(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left_max = post_order(root.left)
            right_max = post_order(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # computing without a split
            global_max[0] = max(global_max[0], root.val + left_max + right_max)
            # computing with a split 
            return root.val + max(left_max, right_max)
        post_order(root)
        return global_max[0]