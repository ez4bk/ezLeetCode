#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        def cmp(a, b):
            return int(b + a) - int(a + b)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if cmp(nums[i], nums[j]) > 0:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int("".join(nums)))


# @lc code=end
