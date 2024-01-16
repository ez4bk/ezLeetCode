#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#


# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        if left > right:
            return [-1, -1]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break

        for i in range(mid, -1, -1):
            if nums[i] != target:
                left = i + 1
                break
        for i in range(mid, len(nums)):
            if nums[i] != target:
                right = i - 1
                break

        if left > right:
            return [-1, -1]
        else:
            return [left, right]


# print(Solution().searchRange([5, 7, 7, 8, 8, 10], 5))

# @lc code=end
