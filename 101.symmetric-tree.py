#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]

        while queue:
            level_size = len(queue)
            a = []
            for i in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    a.append(node.left.val)
                else:
                    a.append(None)
                if node.right:
                    queue.append(node.right)
                    a.append(node.right.val)
                else:
                    a.append(None)
            for i in range(len(a)//2):
                if a[i] != a[-i-1]:
                    return False
        return True

# @lc code=end
