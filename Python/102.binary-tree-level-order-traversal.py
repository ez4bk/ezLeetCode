#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root) -> list[list[int]]:
        from collections import deque
        if not root:
            return []
        queue, res = deque([root]), []

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res

        # @lc code=end
# if __name__ == "__main__":
#     node = TreeNode(3, TreeNode(9, TreeNode(13), None),
#                     TreeNode(20, TreeNode(15), TreeNode(7)))
#     sol = Solution()
#     print(sol.levelOrder(node))
