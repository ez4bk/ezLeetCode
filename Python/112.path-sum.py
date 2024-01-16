#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, target, sum):
            if not root:
                return False
            if not root.left and not root.right:
                return sum + root.val == target
            return dfs(root.left, target, sum + root.val) or dfs(
                root.right, target, sum + root.val
            )

        return dfs(root, targetSum, 0)


# @lc code=end
