#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#


# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        def isSelfDivisible(num: int) -> bool:
            for digit in str(num):
                if digit == "0" or num % int(digit) != 0:
                    return False
            return True

        for num in range(left, right + 1):
            if isSelfDivisible(num):
                res.append(num)
        return res


# @lc code=end
