#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(
            preorder: List[int],
            preStart: int,
            preEnd: int,
            inorder: List[int],
            inStart: int,
            inEnd: int,
        ) -> TreeNode:
            # 前序位置，寻找左右子树的索引
            if preStart > preEnd:
                return None
            rootVal = preorder[preStart]
            index = 0
            for i in range(inStart, inEnd + 1):
                if inorder[i] == rootVal:
                    index = i
                    break
            leftSize = index - inStart
            root = TreeNode(rootVal)

            # 递归构造左右子树
            root.left = build(
                preorder, preStart + 1, preStart + leftSize, inorder, inStart, index - 1
            )
            root.right = build(
                preorder, preStart + leftSize + 1, preEnd, inorder, index + 1, inEnd
            )
            return root

        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


# @lc code=end
