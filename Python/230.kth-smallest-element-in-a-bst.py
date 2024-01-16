#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    order = 0
    res = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: Optional[TreeNode], k: int):
            if root:
                inorder(root.left, k)
                self.order += 1
                if self.order == k:
                    self.res = root.val
                inorder(root.right, k)

        inorder(root, k)
        return self.res


# @lc code=end
