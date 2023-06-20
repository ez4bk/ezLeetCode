#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            res = str(chr(remainder + ord("A"))) + res
        return res


# @lc code=end
