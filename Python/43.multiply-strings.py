#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def decode(num):
            res = 0
            for i in range(len(num)):
                res = res * 10 + ord(num[i]) - ord("0")
            return res

        def encode(num):
            res = ""
            while num:
                res = chr(ord("0") + num % 10) + res
                num //= 10
            return res

        return encode(decode(num1) * decode(num2))


# @lc code=end
