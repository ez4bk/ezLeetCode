#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#


# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator / denominator).is_integer():
            return str(int(numerator / denominator))

        res = ""
        if (numerator < 0) ^ (denominator < 0):
            res += "-"

        numerator, denominator = abs(numerator), abs(denominator)

        res += str(numerator // denominator) + "."

        remainders = {}
        remainder = numerator % denominator

        while remainder != 0 and remainder not in remainders:
            remainders[remainder] = len(res)
            remainder *= 10
            res += str(remainder // denominator)
            remainder %= denominator

        if remainder in remainders:
            res = (
                res[: remainders[remainder]] + "(" + res[remainders[remainder] :] + ")"
            )

        return res


# @lc code=end

print(Solution().fractionToDecimal(-50, 8))
