# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        parent = None
        while curr and curr.val != key:
            parent = curr
            if key > curr.val:
                curr = curr.right
            else:
                curr = curr.left
            
        if not curr:
            return root

            
 
        # one child or zero child
        if not curr.right or not curr.left:
            child = curr.left if curr.left else curr.right

            if root == curr:
                return child

            if parent.right == curr:
                parent.right = child
            else:
                parent.left = child
            return root

        # two children
        # find the minimum in the right subtree
        minimum = curr.right
        parent = curr
        while minimum.left:
            parent = minimum
            minimum = minimum.left

        curr.val = minimum.val
        if parent == curr:
            parent.right = minimum.right
        elif parent != curr:
            parent.left = minimum.right
        return root

        
