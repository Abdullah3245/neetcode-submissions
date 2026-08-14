# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(root):
            left, right = root.left, root.right

            root.left, root.right = right, left

            return 
        def recurse(root : Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return

            swap(root)
            recurse(root.left)
            recurse(root.right)  
            return              

        recurse(root)
        return root

