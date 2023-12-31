#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#


# @lc code=start
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        dup = -1
        missing = 1
        for n in nums:
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
            else:
                nums[abs(n) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]


# @lc code=end
