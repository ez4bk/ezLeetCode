#
# @lc app=leetcode id=108 lang=python3
# @lcpr version=20002
#
# [108] Convert Sorted Array to Binary Search Tree
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not n:
            return None
        mid = n // 2
        return TreeNode(nums[mid],
                        self.sortedArrayToBST(nums[:mid]),
                        self.sortedArrayToBST(nums[mid+1:]))
# @lc code=end



#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#

