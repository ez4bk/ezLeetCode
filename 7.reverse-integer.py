#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        while x:
            rem = x % 10
            res = res * 10 + rem
            x = x // 10
        if res > 2**31 - 1:
            return 0
        return res * flag
# @lc code=end
