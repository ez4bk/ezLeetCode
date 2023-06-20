#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            else:
                two += 1
        nums[:] = [0] * zero + [1] * one + [2] * two


# @lc code=end
