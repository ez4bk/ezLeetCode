#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
            10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
            1000: 'M'
        }
        n = roman.keys()
        res = ''
        while num > 0:
            for i in reversed(n):
                if num >= i:
                    res += roman[i]
                    num -= i
                    break

        return res
# @lc code=end
