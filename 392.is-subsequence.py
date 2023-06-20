#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        for b in t:
            if a == len(s):
                return True
            if b == s[a]:
                a += 1
        return a == len(s)


# @lc code=end
