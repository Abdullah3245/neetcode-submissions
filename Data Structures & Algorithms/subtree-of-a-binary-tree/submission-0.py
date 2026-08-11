# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findSubRoot(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> root:
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            return findSubRoot(root.left, subRoot.left) and findSubRoot(root.right, subRoot.right)
        
        if not root:
            return False
        
        if findSubRoot(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)