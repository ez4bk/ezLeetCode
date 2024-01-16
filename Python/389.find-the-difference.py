#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#


# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Less Memory
        dic = {}
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for c in s:
            dic[c] -= 1
        for c in dic:
            if dic[c] == 1:
                return c

        # Faster Speed
        # xor = 0
        # for cs in s:
        #     xor ^= ord(cs)
        # for ct in t:
        #     xor ^= ord(ct)
        # return chr(xor)


# @lc code=end
