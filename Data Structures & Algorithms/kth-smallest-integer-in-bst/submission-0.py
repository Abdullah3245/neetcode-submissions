# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
      def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kthSmallestHelper(root: Optional[TreeNode], nums : List[int]) -> None:
            if root is None:
                return 
            kthSmallestHelper(root.left, nums)
            nums.append(root.val)
            kthSmallestHelper(root.right, nums)
        nums = []
        kthSmallestHelper(root, nums)
        return nums[k - 1] 
    
        