#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        EZPZ
        """
        a = {}
        for num in nums:
            if a.get(num):
                return True
            else:
                a[num] = 1
        return False


# @lc code=end
