#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        flag = 1
        print(digits)
        for i in range(length-1, -1, -1):
            if flag:
                digits[i] += 1
                if digits[i] > 9:
                    digits[i] = 0
                else:
                    flag = 0
        print(digits)
        if flag == 1:
            digits = [1] + digits

        return digits
# @lc code=end
