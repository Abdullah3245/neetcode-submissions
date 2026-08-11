/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i ++) {
            map.put(inorder[i], i);
        }
        return buildTreeHelper(preorder, 0, 0, inorder.length - 1, map);
    }
    private TreeNode buildTreeHelper(int[] preorder, int start, int left, int right, Map<Integer, Integer> map) {
        TreeNode tree = new TreeNode();
        if (left > right) {
            return null;
        }
        if (right >= preorder.length) {
            return null;
        }
        tree.val = preorder[start];
        int mid = map.get(tree.val);
        tree.left = buildTreeHelper(preorder, start + 1, left, mid - 1, map);
        tree.right = buildTreeHelper(preorder, start + (mid - left) + 1, mid + 1, right, map);
        return tree;
    }  
}
