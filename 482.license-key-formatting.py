#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#


# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        a = ""
        count = k
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                if count == 0:
                    a += "-"
                    count = k
                a += s[i].upper()
                count -= 1
        return a[::-1]


# @lc code=end
