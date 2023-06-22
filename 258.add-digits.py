#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#


# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        a = []
        while num:
            a.append(num % 10)
            num = num // 10
        num = sum(a)
        return self.addDigits(num)

        # O(1) solution
        # return 1 + (num - 1) % 9 if num else 0


# @lc code=end
