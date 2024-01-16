#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        r = 0

        if x < 0:
            return False

        while n > 0:
            r = r * 10 + n % 10
            n = n // 10

        if r == x:
            return True
        return False
        # @lc code=end
