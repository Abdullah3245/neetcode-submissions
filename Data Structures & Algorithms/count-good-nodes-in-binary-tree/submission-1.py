# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        val = root.val

        def dfs(root, max_val):
            if root is None:
                return

            max_val = max(max_val, root.val)
            dfs(root.left, max_val)
            dfs(root.right, max_val)
            
            if max_val == root.val:
                count[0] += 1
        
        dfs(root, -sys.maxsize)
        return count[0]
        