#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#


# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first_max = -1
        second_max = -1
        max_index = -1
        for i in range(len(nums)):
            if nums[i] > first_max:
                first_max, second_max = nums[i], first_max
                max_index = i
            elif nums[i] > second_max:
                second_max = nums[i]
        return -1 if first_max < 2 * second_max else max_index


# @lc code=end
