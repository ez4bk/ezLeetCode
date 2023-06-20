#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = [nums[0]]
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            if nums[i] not in a:
                a.append(nums[i])
        nums[:] = a
        return len(a)
        # @lc code=end
