#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        iMin, iMax = 0, m
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = (m + n + 1) // 2 - i
            if i < m and nums2[j-1] > nums1[i]:
                iMin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                iMax = i - 1
            else:
                if i == 0:
                    maxLeft = nums2[j-1]
                elif j == 0:
                    maxLeft = nums1[i-1]
                else:
                    maxLeft = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    return maxLeft
                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])
                return (maxLeft + minRight) / 2.0

# @lc code=end
