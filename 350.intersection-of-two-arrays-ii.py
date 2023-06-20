#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#


# @lc code=start
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1

        return res


# @lc code=end
