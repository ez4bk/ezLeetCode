#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right + 1):
            res += self.nums[i]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
