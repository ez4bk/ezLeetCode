#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = 1 if dividend ^ divisor >= 0 else -1
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1
        divisor = abs(divisor)
        dividend = abs(dividend)

        multiple = 1
        while dividend >= (divisor << 1):
            divisor <<= 1
            multiple <<= 1

        while multiple > 0:
            if dividend >= divisor:
                dividend -= divisor
                res += multiple
            divisor >>= 1
            multiple >>= 1

        return sign * res


# @lc code=end
