#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while (l < r):
            m = l + (r - l)//2
            if (nums[m] == target):
                return m
            elif (nums[m] > target):
                r = m
            else:
                l = m + 1

        if nums[l] < target:
            return l + 1
        else:
            return l

# @lc code=end
