#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            else:
                # Compute the height of each subtree
                lheight = height(node.left)
                rheight = height(node.right)

            if lheight < 0 or rheight < 0 or abs(lheight - rheight) > 1:
                return -1
            return max(lheight, rheight) + 1

        return height(root) >= 0


# @lc code=end
