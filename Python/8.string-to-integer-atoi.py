#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#

# @lc code=start
from ast import Pow


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        index = 0
        sign = True

        s = s.strip()

        if s == '':
            return 0

        if s[0].isalpha():
            return 0
        elif s[0] == '-':
            sign = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        if s == '':
            return 0

        for i in range(len(s)):
            if not s[i].isnumeric() and s[i] != '.':
                s = s[:i]
                break

        slist = s.split('.')
        if slist[0] == '':
            return 0

        nlist = []
        for i in range(len(slist)):
            nlist.append(int(slist[i]))

        if len(slist) > 1:
            if nlist[1] >= 5 * pow(10, len(slist[1])-1):
                nlist[0] = nlist[0] + 1

        n = nlist[0]
        if not sign:
            n = -n

        if n < -pow(2, 31):
            n = -pow(2, 31)
        if n > pow(2, 31) - 1:
            n = pow(2, 31) - 1

        return n

        # @lc code=end
