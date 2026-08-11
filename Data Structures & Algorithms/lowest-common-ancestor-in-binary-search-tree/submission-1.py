# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            def lowestCommonAncestorHelper(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> TreeNode:

                # Both nodes are in the right subtree
                if p.val > root.val and q.val > root.val:
                    return lowestCommonAncestorHelper(root.right, p, q)

                # Both nodes are in the left subtree
                elif p.val < root.val and q.val < root.val:
                    return lowestCommonAncestorHelper(root.left, p, q)
                    
                # Otherwise either we split or reach p/q itself 
                else:
                    return root

            return lowestCommonAncestorHelper(root, p, q)
        