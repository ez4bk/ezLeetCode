#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in nums:
            if (n-1) in numSet:
                continue
            adder = 1
            while n + adder in numSet:
                adder += 1
            res = max(res, adder)
        return res


# @lc code=end
