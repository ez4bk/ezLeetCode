#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        res = list(nums1 & nums2)

        return res


# @lc code=end
