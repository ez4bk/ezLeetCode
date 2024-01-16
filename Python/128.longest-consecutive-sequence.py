#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, res = set(nums), 0
        for num in s:
            if num - 1 in s:
                continue
            adder = 1
            while num + adder in s:
                adder += 1
            res = max(res, adder)
        return res


# @lc code=end
