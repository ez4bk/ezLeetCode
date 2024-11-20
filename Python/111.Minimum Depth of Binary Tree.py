#
# @lc app=leetcode id=111 lang=python3
# @lcpr version=20002
#
# [111] Minimum Depth of Binary Tree
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left and not root.right:
            return 1
        if not root.left:
            return right + 1
        if not root.right:
            return left + 1
        return min(left, right) + 1
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,null,3,null,4,null,5,null,6]\n
# @lcpr case=end

#

