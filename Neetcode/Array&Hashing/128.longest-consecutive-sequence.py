#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        We put all elements in a set. For each element, we find if
        its consecutive numbers are in the set.
        
        !!! Note we need to locate the head of the consecutive sequence,
        so if (n - 1) exists in the set, although it is a member of
        a potential result, we ignore it to find the head of the sequence.
        """
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
