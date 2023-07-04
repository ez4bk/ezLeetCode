#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) < len(num2):
            num1 += "0" * (len(num2) - len(num1))
        else:
            num2 += "0" * (len(num1) - len(num2))

        res = ""
        carry = 0
        for i in range(len(num1)):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            carry = digit_sum // 10
            res += str(digit_sum % 10)

        if carry > 0:
            res += str(carry)

        return res[::-1]


# @lc code=end
