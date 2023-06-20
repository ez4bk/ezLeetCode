#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#


# @lc code=start
class Solution:
    def thirdMax(self, nums) -> int:
        if len(nums) < 3:
            return max(nums)

        maxnum = float("-inf")
        second = float("-inf")
        third = float("-inf")

        for i in range(len(nums)):
            if nums[i] > maxnum:
                third = second
                second = maxnum
                maxnum = nums[i]
            elif nums[i] > second and nums[i] < maxnum:
                third = second
                second = nums[i]
            elif nums[i] > third and nums[i] < second:
                third = nums[i]

        return third if third != float("-inf") else maxnum


# @lc code=end
